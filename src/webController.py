import time

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class webControllerOption:
    def __init__(self, dpt_dt, dpt_tm, dpt_sta, arv_sta):
        self.dpt_dt = dpt_dt
        self.dpt_tm = dpt_tm
        self.dpt_sta = dpt_sta
        self.arv_sta = arv_sta
        self.check_suite = True
        self.observe_num_of_items = 5

    def set_observe_num_of_items(self, value):
        self.observe_num_of_items = value

    def set_check_suite(self, value):
        self.check_suite = value


class webController:
    def __init__(self, option: webControllerOption):
        # 변수 설정
        self.is_logged_in = False
        self.option = option
        
        # detach option 추가
        options = Options()
        options.add_experimental_option("detach", True)
        
        # driver 설정
        self.driver = webdriver.Chrome(options=options)

    def login(self, email, password):
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

        escape = False
        while not escape:
            # 조회 폼 가져오기
            search_form = driver.find_element('name', 'search-form')

            # 조회 submit
            search_form.submit()

            try:
                # 로딩 기다리기
                driver.implicitly_wait(5)
                # 나머지 요소들 로딩을 위해 1초 기다림
                time.sleep(1)
            # timeout 시 return false
            except TimeoutError:
                return False

            # option에서 지정한 갯수만큼 위에서 검사
            for i in range(self.option.observe_num_of_items):
                xpaths = [
                    # 일반실 예약하기 버튼 내 span xpath
                    f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{i + 1}]/td[7]/a/span',
                    # 특실 예약하기 버튼 내 span xpath
                    f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{i + 1}]/td[6]/a/span',
                ]

                # 지정된 xpath를 순회
                for xpath in xpaths:
                    # span 추출
                    spans = driver.find_elements('xpath', xpath)
                    # span이 있고, text가 예약하기라면
                    if len(spans) and spans[0].text == '예약하기':
                        # 부모 element를 클릭
                        spans[0].find_element('xpath', '..').click()
                        return True

        return True

    def close(self):
        self.driver.close()

    def is_closed(self):
        try:
            _ = self.driver.current_window_handle
            return False
        except:
            return True
