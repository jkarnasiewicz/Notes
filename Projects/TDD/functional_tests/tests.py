# test funkcjonalny == test akceptacji == test E2E
# testy funkcjonalne są przeznaczone do testowania aplikacj z zewnątrz, z perespektywy jej użytkownika

# testy jednostkowe sprawdzają aplikację z wewnątrz, z perespektywy programisty
# testy jednostkow są sterowane testami funkcjonalnymi

# refaktoryzacja - próba ulepszenia kodu bez wprowadzania zmian w jego funkcjonalności

# proces TDD :
# test funkcjonalny
# test jednostkowy(konfiguracja, sprawdzenie, asercja)
# cykl test jednostkowy i tworzenie kodu
# refaktoryzacja

# import unittest
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	# setUp() and tearDown() runs before and after each test 
	# like context-manager protocol
	# __enter__(self)
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	# __exit__(self, exc_type, exc_object, exc_traceback))
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# self.browser.get('http://127.0.0.1:8000')
		self.browser.get(self.live_server_url)

		self.assertIn('Listy', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('listę', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Wpisz rzeczy do zrobienia')


		inputbox.send_keys('Kupić pawie pióra')
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Użyć pawich piór do zrobienia przynęty')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Kupić pawie pióra')
		self.check_for_row_in_list_table('2: Użyć pawich piór do zrobienia przynęty')

		# self.fail('Zakończenie testu!')
		self.browser.implicitly_wait(3)
		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Kupić pawie pióra', page_text)
		self.assertNotIn('zrobienia przynęty', page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Kupić mleko')
		inputbox.send_keys(Keys.ENTER)

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Kupić pawie pióra', page_text)
		self.assertIn('Kupić mleko', page_text)

# Jeśli nie używamy silnika django
# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')
