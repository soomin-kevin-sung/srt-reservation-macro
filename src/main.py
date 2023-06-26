from selenium.webdriver.support.ui import Select
from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    url = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
    driver.get(url)
    page_source = driver.page_source

    # 선작업
    driver.execute_script(
        'document.getElementsByName(\'dptDt\')[0]' +
        '.removeAttribute(\'readonly\')')

    start_selector = Select(driver.find_element('name', 'dptRsStnCd'))
    end_selector = Select(driver.find_element('name', 'arvRsStnCd'))
    start_date_input = driver.find_element('name', 'dptDt')
    psg_adults_selector = Select(driver.find_element('name', 'psgInfoPerPrnb1'))
    psg_children_selector = Select(driver.find_element('name', 'psgInfoPerPrnb5'))
    search_button = driver.find_element('xpath', '//*[@id="search-form"]/fieldset/a')

    start_selector.select_by_visible_text('수서')
    end_selector.select_by_visible_text('부산')

    start_date_input.clear()
    start_date_input.send_keys('2023.06.29')

    psg_adults_selector.select_by_index(0)
    psg_children_selector.select_by_index(1)

    search_button.click()
    while True:
        pass


if __name__ == '__main__':
    main()
