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










# TestCase - before running each test, django resets the database to its initial state
# The individual tests are performed to the first error (poszczególne testy wykonują sie do pierwszego błedu)
import unittest
from django.test import TestCase, LiveServerTestCase, modify_settings, override_settings
# from django.contrib.auth import get_user_model, SESSION_KEY

class TestSomething(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        # allows the creation of initial data at the class level, once for the whole TestCase
        # this technique allows for faster tests as compared to using setUp()
        # if the tests are run on a database with no transaction support, setUpTestData() will be
        # called before each test, negating the speed benefits

    @classmethod
    def setUpClass(cls):
        # create test configuration for the class (it will be executed only once)
        super(TestSomething, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        # cleaning up test configuration for the class (it will be executed only once)

    def setUp(self):
        # this method will be run before each test method

    def tearDown(self):
        # this method will be run after each test method, irrespective of whether the test passed or not

        for method, error in self._outcome.errors:
            if error:
                ...                                         # more TDD 372
        super().tearDown()

    # django
    def test_django(self):                                  # any method whose name starts with 'test' will be executed as a test method
        self.assertEqual(Item.objects.count(),  1, msg)     # if values are not equal it will throw an AssertionError
        self.assertTrue(element in self.nums, msg)          # verify the condition
        self.assertLess(element, 4, "not less")

        self.assertRaises(                                  # verify that an expected exception gets raised
            TypeError, random.shuffle, (1, 2, 3))
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()                               # metoda przeznaczona do recznego wykonania pelnej operacji sprawdzenia

        with self.assertRaisesRegexp(ValidationError, 'Enter a valid URL.'):    # Error contains provided message
            ...

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


# unnecessary when using django test engine
if __name__ == "__main__":
    unittest.main()
    # unittest.main(warnings='ignore')


# Creating custom test runners (Python Unlock(99))
unittest.main(verbosity=2, testRunner=XMLRunner)

# Running test cases in parallel
# The py.test library has an xdist plugin, which adds the capability to run tests in parallel










# subTest
# parameterization - manageable inputs to tests
def convert(alpha):
    return ','.join([str(ord(i)-96) for i in alpha])

class TestOne(unittest.TestCase):
    def test_system(self):
        cases = [("aa","1,1"),("bc","2,3"),("jk","4,5"),("xy","24,26")]
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(convert(case[0]),case[1])










# Mocks (Imitacja) - tworzenie fikcyjnej implementacji API

# Mock are objects that can test the behavior, and stubs are
# simply placeholder implementations
from unittest.mock import Mock, patch, create_autospec

mock_obj = Mock()
mock_obj.return_value
mock_obj.side_effect
# assert that the mock was called exactly once and with the specified arguments (TDD 345)
mock_obj.assert_called_once_with(*args, **kwargs)





# create_autospec - for ensuring that the mock objects in your tests have the
# same api as the objects they are replacing, you can use auto-speccing
class TestWorkerReporting(unittest.TestCase):

    def test_worker_busy(self,):
        # mock_function = create_autospec(function, return_value='fishy')
        mworker = create_autospec(IWorker)
        mworker.configure_mock(**{'is_busy.return_value':True})
        self.assertFalse(assign_if_free(mworker, {}))





class TestMocks(TestCase):
    def test_checks_superhero_service_obj(self):
        with patch("profiles.models.SuperHeroWebAPI") as ws:
            ws.is_hero.return_value = True
            user = User.objects.create_user(username="ivy")
            check_superhero = user.profile.is_superhero()
        ws.is_hero.assert_called_with('ivy')
        self.assertTrue(check_superhero)

    @patch('accounts.views.authenticate')
    def test_calls_authenticate_with_assertion_from_post(
            self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'assert this'})
        mock_authenticate.assert_called_once_with(assertion='assert this')

    @patch('accounts.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(
            self, mock_authenticate):
        user = User.objects.create(email='a@b.com')
        user.backend = ''  # required for auth_login to work
        mock_authenticate.return_value = user
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(self.client.session[SESSION_KEY], str(user.pk))










# Fixtures
class TestMocks(TestCase):
    fixtures = ['posts.json']

# factory class
class PostFactory:

    def make_post(self):
        return Post.objects.create(message="")

class PostTestCase(TestCase):

    def setUp(self):
        self.blank_message = PostFactory().makePost()

    def test_some_post_functionality(self):
        pass










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










# Coverage.py
coverage run manage.py test apps
coverage html                           # see htmlcov/index.html



# Additional informations

# Here are some qualities of a good test case (which is a subjective term, of course)
# in the form of an easy-to-remember mnemonic "F.I.R.S.T. class test case":
1. Fast: the faster the tests, the more often they are run. Ideally, your tests
should complete in a few seconds
2. Independent: Each test case must be independent of others and can be
run in any order
3. Repeatable: The results must be the same every time a test is run. Ideally,
all random and varying factors must be controlled or set to known values
before a test is run
4. Small: Test cases must be as short as possible for speed and ease of
understanding
5. Transparent: Avoid tricky implementations or ambiguous test cases



# Perhaps, even more important are the don'ts to remember while writing test cases:
1. Do not (re)test the framework: Django is well tested. Dont check for URL
lookup, template rendering, and other framework-related functionality
2. Do not test implementation details: Test the interface and leave the minor
implementation details. It makes it easier to refactor this later without
breaking the tests
3. Test models most, templates least: Templates should have the least business
logic, and they change more often
4. Avoid HTML output validation: Test views use their context variables
output rather than its HTML-rendered output
5. Avoid using the web test client in unit tests: Web test clients invoke several
components and are therefore, better suited for integration tests
6. Avoid interacting with external systems: Mock them if possible. Database is
an exception since test database is in-memory and quite fast



# Fast testing
from django.test import Client
Client().get("http://0.0.0.0:8000/public/").content



# Assertions methods
https://docs.python.org/3/library/unittest.html
https://docs.djangoproject.com/en/1.10/topics/testing/tools/



# Libraries: py.test, nose and factory_boy(fixtures)
