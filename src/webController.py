import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver


class webControllerOption:
    def __init__(self, dpt_dt, dpt_tm, dpt_sta, arv_sta, check_suite):
        self.dpt_dt = dpt_dt
        self.dpt_tm = dpt_tm
        self.dpt_sta = dpt_sta
        self.arv_sta = arv_sta
        self.check_suite = check_suite


class webController:
    def __init__(self, option: webControllerOption):
        self.driver = webdriver.Chrome()
        self.is_logged_in = False
        self.option = option

    def login(self, email, password):
        from selenium.common import NoAlertPresentException

        driver = self.driver
        driver.get('https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000')

        # email 라디오 버튼 클릭
        driver.find_element('id', 'srchDvCd2').click()

        # email 입력
        email_input = driver.find_element('id', 'srchDvNm02')
        email_input.clear()
        email_input.send_keys(email)

        # password 입력
        passwd_input = driver.find_element('id', 'hmpgPwdCphd02')
        passwd_input.clear()
        passwd_input.send_keys(password)

        # 버튼 클릭
        driver.find_element('xpath', '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[3]/div/div[2]/input').click()

        # 로그인 실패 시 (경고창 발생)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            self.is_logged_in = False
            return False
        except NoAlertPresentException:
            self.is_logged_in = True
            return True

    def run_macro(self):
        if not self.is_logged_in:
            raise Exception('로그인이 필요합니다.')

        driver = self.driver
        driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000')

        # 출발역 설정
        dpt_sta_input = driver.find_element('name', 'dptRsStnCdNm')
        dpt_sta_input.clear()
        dpt_sta_input.send_keys(self.option.dpt_sta)

        # 도착역 설정
        arv_sta_input = driver.find_element('name', 'arvRsStnCdNm')
        arv_sta_input.clear()
        arv_sta_input.send_keys(self.option.arv_sta)

        # 날짜 설정
        date_selector = Select(driver.find_element('name', 'dptDt'))
        date_selector.select_by_value(self.option.dpt_dt)

        # 시간 설정
        time_selector = Select(driver.find_element('name', 'dptTm'))
        time_selector.select_by_value(self.option.dpt_tm)

        is_success = False
        while not is_success:
            # 조회 폼 사용
            search_form = driver.find_element('name', 'search-form')
            search_form.submit()
            driver.implicitly_wait(5)
            time.sleep(0.5)


