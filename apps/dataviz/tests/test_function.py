from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

import time


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = "/usr/bin/firefox"

        cls.browser = webdriver.Firefox(capabilities=caps)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def _login_input(self):
        login_input = self.browser.find_element_by_id('id_username')
        self.assertIsNotNone(login_input, 'Username input absent')
        password_input = self.browser.find_element_by_id('id_password')
        self.assertIsNotNone(password_input, 'Password input absent')
        submit_input = self.browser.find_element_by_xpath('//input[@type="submit" and @value="Log in"]')
        self.assertIsNotNone(submit_input, 'Login input button absent')
        return login_input, password_input, submit_input

    def test_user_and_csv(self):
        # user visit home page of DataViz
        self.browser.get('http://localhost:8000')
        # user notice that title of page contain 'DataViz'
        self.assertIn('DataViz | Login', self.browser.title, "Browser title was " + self.browser.title)
        # also there are field to enter login
        # and password
        # of course there are login button
        login_input, password_input, submit_input = self._login_input()
        # user enter incorrect login and password
        login_input.send_keys('test')
        password_input.send_keys('test')
        submit_input.click()
        # and notice alert about incorrect login or password
        error_msg = self.browser.find_element_by_class_name('error')
        self.assertIn(error_msg.text, "Your username and password didn't match. Please try again.")
        # user enter correct login and password
        login_input, password_input, submit_input = self._login_input()
        login_input.clear()
        login_input.send_keys('admin')
        password_input.send_keys('createsuperuser')
        submit_input.click()
        time.sleep(1)
        # and was redirected to DataViz page
        self.assertIn('DataViz | Home', self.browser.title, "Browser title was " + self.browser.title)
        # user notice that there is two tab on page
        # one 'DataViz' second 'Data Upload'
        # DataViz tab open by default
        # 'no data available for visualization' message shown
        self.assertIn('no data available for visualization', self.browser.page_source)
        # user click on 'Data Upload' tab

        # upload file in csv format

        # after successful file upload
        # statistic shown

        # user switch to 'DataViz' tab
        # on tab user select Region from drop-down menu

        # bar-chart shown

        # user select other region and chart change
        self.fail('Finish the test!')
