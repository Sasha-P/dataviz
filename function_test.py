from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = "/usr/bin/firefox"

        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_config_correctly(self):
        self.browser.get('http://localhost:8000')

        assert 'Django' in self.browser.title, "Browser title was " + self.browser.title


if __name__ == '__main__':
    unittest.main(warnings='ignore')
