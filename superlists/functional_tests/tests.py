from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


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

    def wait_for_row_in_list_table(self, row_text):
        """ wait for row in list table"""

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        """ test: can start a list for one user """

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

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.wait_for_row_in_list_table('1: Buy simple bird')

        # input "Buy birdcage"
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys('Buy birdcage')
        input_box.send_keys(Keys.ENTER)

        # press <Enter> page refreshed and body contains two elements list
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.wait_for_row_in_list_table('1: Buy simple bird')
        self.wait_for_row_in_list_table('2: Buy birdcage')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """ test_multiple_users_can_start_lists_at_different_urls """

        # start new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy simple bird')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy simple bird')

        # list has unique url
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # new user start
        self.browser.quit()
        self.browser = webdriver.Firefox(options=self.options)

        # get home page, page not present other user data
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy simple bird', page_text)
        self.assertNotIn('Buy birdcage', page_text)

        # new list create
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # getting new url
        new_url = self.browser.current_url
        self.assertRegex(new_url, '/lists/.+')
        self.assertNotEqual(new_url, edith_list_url)

        # not mark first list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy simple bird', page_text)
        self.assertIn('Buy milk', page_text)


