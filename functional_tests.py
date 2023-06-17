from selenium import webdriver
import unittest


class NewVisitorsTest(unittest.TestCase):
    """ test new visitor """

    def setUp(self) -> None:
        self.set_options()
        self.browser = webdriver.Firefox(options=self.options)

    def set_options(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--width=300")
        self.options.add_argument("--height=500")

    def tearDown(self) -> None:
        self.browser.quit()
        self.fail('Test final')

    def test_can_start_a_list_and_retrieve_if_later(self):
        """ test can start a list and retrieve if later """

        # open home page
        self.browser.get('http://localhost:8000')

        # title exists To-Do label
        self.assertIn('To-Do', self.browser.title)

        # can edit element content

        # input "Buy simple bird"

        # press <Enter> page refreshed and body contains "1: Buy simple bird"

        # input "Buy birdcage"

        # press <Enter> page refreshed and body contains two elements list

        # site contains unique url for link at the birds list

        # press list url and see our birds list on the page

        # close browser







if __name__ == '__main__':
    unittest.main(warnings='ignore')
