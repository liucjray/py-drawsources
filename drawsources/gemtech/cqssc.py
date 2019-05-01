import os

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
url = 'http://www.gem-ds.com/lottery.html?lottery=cqssc'

options = ChromeOptions()
options.headless = True
browser = webdriver.Chrome(chrome_driver_path, options=options)
delay = 1
try:
    browser.get(url)
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'table-ball')))
    wait = WebDriverWait(browser, delay)

    issues = []
    issuesElements = browser.find_elements_by_css_selector('.lottery-table td:nth-child(2)')
    for element in issuesElements:
        issues.append(element.get_attribute('innerHTML'))
    print(issues)

    codes = []
    codesElements = browser.find_elements_by_css_selector('.lottery-table td:nth-child(3)')
    for element in codesElements:
        tmpCodes = element.find_elements_by_class_name('table-ball')
        issueCodes = []
        for tmpCode in tmpCodes:
            issueCodes.append(tmpCode.get_attribute('innerHTML'))
        codes.append(','.join(issueCodes))
    print(codes)

finally:
    browser.close()
