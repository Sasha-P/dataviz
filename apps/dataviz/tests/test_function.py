from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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

    def test_user_and_csv(self):
        # user visit home page of DataViz
        self.browser.get('http://localhost:8000')
        # user notice that title of page contain 'DataViz'
        self.assertIn('DataViz', self.browser.title, "Browser title was " + self.browser.title)
        self.fail('Finish the test!')
        # also there are field to enter login
        # and password
        # ofcorse there are login button

        # user enter incorrect login and password

        # and notice alert about incorrect login or password

        # user enter correct login and password

        # and was redirected to DataViz page

        # user notice that there is two tab on page
        # one 'DataViz' second 'Data Upload'
        # DataViz tab open by default
        # 'no data available for visualization' message shown

        # user click on 'Data Upload' tab

        # upload file in csv format

        # after successful file upload
        # statistic shown

        # user switch to 'DataViz' tab
        # on tab user select Region from drop-down menu

        # bar-chart shown

        # user select other region and chart change
