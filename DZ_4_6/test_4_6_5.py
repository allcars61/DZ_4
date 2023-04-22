# Применив selenium, напишите unit-test для авторизации на Яндексе
# по url: https://passport.yandex.ru/auth/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestYandexAuthorization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_authorization(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://passport.yandex.ru/auth/")
        elem = driver.find_element_by_id("passp-field-login")
        elem.send_keys("your_username")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("passp-field-passwd")
        elem.send_keys("your_password")
        elem.send_keys(Keys.RETURN)
        assert "Yandex" in driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()