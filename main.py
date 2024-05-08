import time
from browser import Browser

if __name__ == '__main__':
    browser = Browser()
    browser.setup()
    browser.login()
    time.sleep(2)
    browser.fill_missing_days("07/05/2024", "07/05/2024")
    time.sleep(1)
    browser.close()
