from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.im_page import ImPage


class LoginPage(BasePage):
    _ip = "192.168.10.32"
    _base_url = r"http://{}/dwcta/study-list" % _ip
    _user = (By.CSS_SELECTOR, 'input[placeholder="用户名"]')
    _pw = (By.CSS_SELECTOR, 'input[placeholder="密码"]')
    _login = (By.CSS_SELECTOR, 'button[type="submit"]')
    _member = (By.CSS_SELECTOR, '.el-checkbox__inner')

    def login(self,user,pw):
        self.find(self._user).send_keys(user)
        self.find(self._pw).send_keys(pw)
        self.find(self._login).click()
        return ImPage(self._driver)





