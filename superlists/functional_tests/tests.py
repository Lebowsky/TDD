from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorsTest(LiveServerTestCase):
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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_if_later(self):
        """ test can start a list and retrieve if later """

        # open home page
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: Buy simple bird')

        # input "Buy birdcage"
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Buy birdcage')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # press <Enter> page refreshed and body contains two elements list
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.check_for_row_in_list_table('1: Buy simple bird')
        self.check_for_row_in_list_table('2: Buy birdcage')

        # site contains unique url for link at the birds list

        # press list url and see our birds list on the page

        # close browser

        self.fail('Test final')

