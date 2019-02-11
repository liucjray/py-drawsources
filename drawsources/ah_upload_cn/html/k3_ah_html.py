import os
import time
from settings import env
from drawsources.ah_upload_cn.html import *
from lib.sources.SourceAHFC import *


def get_instance():
    chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
    url = 'http://ah.uplottery.cn/zst/ah_k3_pc/jb?key='
    options = ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(chrome_driver_path, options=options)

    try:
        browser.get(url)

        issues = []
        issuesElements = browser.find_elements_by_css_selector('.term-scroller table:nth-child(1) tr td')
        for element in issuesElements:
            issues.append(element.get_attribute('innerHTML'))

        # 移除無用資訊
        issues = issues[0:-5]

        # 休息一秒確保號碼全部出現
        time.sleep(1)

        codes = []
        trs = browser.find_elements_by_css_selector('#base-table tbody:nth-child(1) tr')
        for tr in trs:
            issueCodes = []
            tds = tr.find_elements_by_tag_name('td')
            for td in tds[0:3]:
                code = td.find_element_by_tag_name('span').get_attribute('innerHTML')
                issueCodes.append(code)
            codes.append(','.join(issueCodes))

        result = dict(zip(issues, codes))

        return SourceAHFC({
            'data': result,
            'resource': 'ahfc',
            'area': 'ah',
            'type': 'k3',
        })

    finally:
        browser.close()
