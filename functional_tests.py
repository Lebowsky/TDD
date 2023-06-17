from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
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


    def test_can_start_a_list_and_retrieve_if_later(self):
        """ test can start a list and retrieve if later """

        # open home page
        self.browser.get('http://localhost:8000')

        # title exists To-Do label
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(by=By.TAG_NAME, value='h1').text
        self.assertIn('To-Do', header_text)

        # can edit element content
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # input "Buy simple bird"
        input_box.send_keys('Buy simple bird')

        # press <Enter> page refreshed and body contains "1: Buy simple bird"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy simple bird' for row in rows)
        )

        # input "Buy birdcage"

        # press <Enter> page refreshed and body contains two elements list

        # site contains unique url for link at the birds list

        # press list url and see our birds list on the page

        # close browser

        self.fail('Test final')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
