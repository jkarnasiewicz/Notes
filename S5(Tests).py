Testy Funkcjonalne (Functional tests)
# test funkcjonalny == test akceptacji == test E2E
# testy funkcjonalne są przeznaczone do testowania aplikacj z zewnątrz, z perespektywy jej użytkownika

Testy Zintegrowane (Integrated tests) oparte na ORM lub kliencie testów django
Testy Odizolowane (Isolated tests) stosujące imitacje (mock)                    # testy jednostkowe (unit tests)
# testy zintegrowane/odizolowane sprawdzają aplikację z wewnątrz, z perespektywy programisty
# testy zintegrowane/odizolowane są sterowane testami funkcjonalnymi



# Proces TDD:
test funkcjonalny
testy zintegrowane/odizolowane (konfiguracja, sprawdzenie, asercja)
cykl test zintegrowany/odizolowany i tworzenie kodu
refaktoryzacja - próba ulepszenia kodu bez wprowadzania zmian w jego funkcjonalności



# Informacje:
Poszczególne testy wykonują sie do pierwszego błedu



# Imitacja (Mock) - tworzenie fikcyjnej implementacji API
from unittest.mock import patch, Mock

mock_obj = Mock()
mock_obj.return_value
mock_obj.side_effect
mock_obj.assert_called_once_with()                          # czy funkcja zostala wywolana z nastepujacymi argumentami (TDD 345)



import unittest
# from django.test import TestCase, LiveServerTestCase, modify_settings, override_settings
# from unittest.mock import patch
# from django.contrib.auth import get_user_model, SESSION_KEY       # User = get_user_model()
class TestSomething(unittest.TestCase):

    @classmethod
    def setUpClass(cls):                                    # Create test configuration for the class (it will be executed only once)
        ...

    @classmethod
    def tearDownClass(cls):
        ...

    def setUp(self):							            # setUp() and tearDown() runs before and after each test 
	   ...

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                ...                                         # more TDD 372
        super().tearDown()

    # django
    def test_django(self):                                  # all methods that starts with 'test' will be run as the tests
        self.assertEqual(Item.objects.count(),  1, msg)     # if values are not equal it will throw an AssertionError
        self.assertTrue(element in self.nums, msg)          # verify the condition

        self.assertRaises(                                  # verify that an expected exception gets raised
            TypeError, random.shuffle, (1, 2, 3))
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()                               # metoda przeznaczona do recznego wykonania pelnej operacji sprawdzenia

        self.assertContains(response, 'name="text"')
        self.assertNotContains(response, 'item 3')

        self.assertIn('number', response.context['form'].form.errors)

        # found = resolve('/')
        # self.assertEqual(found.func, my_view)
        self.assertEqual(response.resolver_match.func, my_view)

        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        # response = home_page(request)                     # context = RequestContext(request)
        response = self.client.post('/home_page/', data={'item_text': 'A new list item'})
        response = self.client.get(reverse('home_page'), {'district': 'EU'}, follow=True)

        # request = HttpRequest() 
        # response = home_page(request)
        # expected_html = render_to_string('home.html', {'form': ItemForm()})
        # self.assertEqual(response.content.decode(), expected_html)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        # self.assertTrue('home.html' in [temp.name for temp in response.templates])

        self.assertIsInstance(response.context['form'], ItemForm)

        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response, '/lists/{}/'.format(item.id))
        self.assertRedirects(response, '/admin/coupons/coupontemplate/', status_code=302, target_status_code=200)
        self.assertRedirects(response, reverse('item_detail', kwargs={'item': item.pk}))
        
        self.client.login(username='john', password='blowfish')
        self.client.force_login(self.super_user)
        self.client.logout()

        response.redirect_chain
        response.request['PATH_INFO']

    @modify_settings(
        MIDDLEWARE_CLASSES={
            'prepend': 'django.middleware.cache.UpdateCacheMiddleware',
            'append': MIDDLEWARE_CLASSES})
    def test_modify_settings(self):
        pass

    @override_settings(
        DEBUG=True,
        TEMPORARY_UNAVAILABLE=True,
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
        CELERY_ALWAYS_EAGER=True,
        BROKER_BACKEND='memory')
    def test_override_settings(self):
        pass


    # Skip
    @unittest.skip("not needed")
    def test_not_needed(self):
        pass


    # Mock
    @patch('accounts.views.authenticate')
    def test_calls_authenticate_with_assertion_from_post(
        self, mock_authenticate
    ):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'assert this'})
        mock_authenticate.assert_called_once_with(assertion='assert this')

    @patch('accounts.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(
        self, mock_authenticate
    ):
        user = User.objects.create(email='a@b.com')
        user.backend = ''  # required for auth_login to work
        mock_authenticate.return_value = user
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(self.client.session[SESSION_KEY], str(user.pk))

        
 
if __name__ == "__main__":                                  # unnecessary when using django test engine
	unittest.main()
    # unittest.main(warnings='ignore')










# Functional Test
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id),
            'Could not find element with id {}. Page text was:\n{}'.format(
                element_id, self.browser.find_element_by_tag_name('body').text
            )
        )

    def wait_to_be_logged_in(self):
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)

    def test_login_with_persona(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        self.switch_to_new_window('Mozilla Persona')

        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        self.switch_to_new_window('To-Do')

        self.wait_to_be_logged_in()

        self.browser.refresh()
        self.wait_to_be_logged_in()

    @patch('accounts.authentication.requests.post')
    def test_logs_non_okay_responses_from_persona(self, mock_post):
        response_json = {
            'status': 'not okay', 'reason': 'eg, audience mismatch'
        }
        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = response_json

        logger = logging.getLogger('accounts.authentication')
        with patch.object(logger, 'warning') as mock_log_warning:
            self.backend.authenticate('an assertion')

        mock_log_warning.assert_called_once_with(
            'Persona says no. Json was: {}'.format(response_json)
        )
