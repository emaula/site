from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import unittest
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_menu(self, menu_text):
        start_time = time.time()
        while True:
            try:
                menus = self.browser.find_elements_by_class_name('nav-item')
                self.assertIn(menu_text, [menu.text for menu in menus])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_find_homepage_with_the_right_content(self):
        # A teacher hears about EmAula.xyz and goes to the homepage to check it out
        self.browser.get(self.live_server_url)
        self.assertIn('EmAula.xyz | Planeje e compartilhe suas aulas!', self.browser.title)

        # In the homepage, the teacher looks around and wants to learn more
        # about the project. They find the following pages:
        # Sobre (About)
        self.wait_for_menu('Sobre')

        # Equipe (Team)
        self.wait_for_menu('Equipe')

        # Colabore! (Colaborate)
        self.wait_for_menu('Colabore!')

    def test_can_register_with_the_website(self):
        # The teacher doesn't have a password yet,
        # so they must register with the website
        self.browser.get(self.live_server_url)

        # Register (Inscreva-se!)
        registration = self.browser.find_element_by_link_text('Inscreva-se!')
        registration.click()

        time.sleep(1)

        # The teacher fills out their details
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('christann')
        first_name = self.browser.find_element_by_id('id_first_name')
        first_name.send_keys('Chris')
        last_name = self.browser.find_element_by_id('id_last_name')
        last_name.send_keys('Ann')
        email = self.browser.find_element_by_id('id_email')
        email.send_keys('cris@zemail.com')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('1a2b3c4d5e6f7g8H9i0Jk')
        password.send_keys(Keys.ENTER)

        time.sleep(1)

        # They go back to the homepage to login
        home = self.browser.find_element_by_id('home')
        home.click()

        # To-do: redirect to home_page after x seconds.

    def test_teacher_can_login_to_the_emaula_system(self):
        self.browser.get(self.live_server_url)

        # In the homepage, the teacher finds an input for the login
        username = self.browser.find_element_by_id('username')
        username.send_keys('chris_ann')
        self.assertEqual(
            username.get_attribute('placeholder'),
            'Login'
        )

        # And an input for the password
        password = self.browser.find_element_by_id('password')
        password.send_keys('1a2b3c4d5e6f7g8H9i0Jk')
        self.assertEqual(
            password.get_attribute('placeholder'),
            'Senha'
        )
        password.send_keys(Keys.ENTER)
