from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

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
        self.browser.get('http://localhost:8000')
        self.assertIn('EmAula.xyz | Planeje e compartilhe suas aulas!', self.browser.title)

        # In the homepage, the teacher finds the following menus:
        # Sobre (About)
        self.wait_for_menu('Sobre')

        # Equipe (Team)
        self.wait_for_menu('Equipe')

        # Colabore! (Colaborate)
        self.wait_for_menu('Colabore!')

        # Inscreva-se! (Register)
        self.wait_for_menu('Inscreva-se!')

        # The teacher also finds an inputbox to login into the EmAula system
        inputbox = self.browser.find_element_by_id('username')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Login'
        )

        # And an inputbox for the password
        inputbox = self.browser.find_element_by_id('password')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Senha'
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
