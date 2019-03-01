Testy Funkcjonalne (Functional tests)
# test funkcjonalny == test akceptacji == test E2E
# testy funkcjonalne są przeznaczone do testowania aplikacj z zewnątrz, z perespektywy jej użytkownika

Testy Zintegrowane (Integrated tests) oparte na ORM lub kliencie testów django
Testy Odizolowane (Isolated tests) stosujące imitacje (mock)                    # testy jednostkowe (unit tests)
# testy zintegrowane/odizolowane sprawdzają aplikację z wewnątrz, z perespektywy programisty
# testy zintegrowane/odizolowane są sterowane testami funkcjonalnymi



# Proces TDD:
1. test funkcjonalny
2. testy zintegrowane/odizolowane (konfiguracja, sprawdzenie, asercja)
3. cykl test zintegrowany/odizolowany i tworzenie kodu
4. refaktoryzacja - próba ulepszenia kodu bez wprowadzania zmian w jego funkcjonalności

# Za kazdym razem gdy pojawi sie nowe wymaganie, w pierwszej kolejnosci powinny byc zmodyfikowane testy.
# Uruchomienie testów bedzie testem, ktory potwierdzi(bądź nie) potrzebe wprowadzenia kolejnych zmian w implementacji
# testowanej funkcji
1. Napisanie automatycznych testów(funkcjonalnych/zintegrowanych/odizolowanych) dla nowej funkcjonalności lub usparwnienia,
   ktore jeszcze nie są zaimplementowane
2. Dostarczanie minimalnej implementacji spełniającej wymagania wyrażone testami
3. Refaktoryzacja kodu w celu osiągnięcia  pożądanego poziomu jakości

# Zalety TDD
1. Pozwala ograniczyć zjawisko regresji w kodzie
# regresja - blad ktory byl wczesniej rozwiazany, lub taki ktory dotyczy funkcjonalnosci dzialajacych dotychczas bezproblemowo
2. Podnosi jakość kodu
# pisanie testów, które w większości przypadków są przykładami użycia dla kodu, pozwala utrzymywać punkt widzenia uzytkownika
# tworzonych interfejsów programistycznych (weryfikacja zasadności doboru nazw, argumentów czy struktur interfejsów)
3. Umozliwia tworzenie bardziej niezawodnego oprogramowania w krótszych cyklach
# pisanie kodu bez testów wydłuża proces wyszukiwania i naprawiania błędów
4. Testy pełnią dodatkową funkcję niskopoziomowej dokumentacji przypadków użycia kodu
# testy sa najlepszym miejscem, gdzie programista moze sie dowiedziec, jak dziala dane oprogramowanie
# czasami taki przykład wart jest więcej niż tysiąc słów

# Izolacja ma zapewnić
1. testy odnosza się do atomowych części aplikacji, czyli funkcji, metod, klas lub interfejsów
2. cały proces jest deterministyczny i powtarzalny



# python -m unittest file_name.py -v
import sys
from random import shuffle
import unittest


# To handle especially expensive setup operations for all of the tests within
# a module use the module-level functions setUpModule() and tearDownModule()
def setUpModule():
    print('In setUpModule()')

def tearDownModule():
    print('In tearDownModule()')


class SimpleTest(unittest.TestCase):

    # Fixtures for all instances of a test class
    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        # cls.good_range = range(1, 10)

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        # del cls.good_range

    # Fixtures for each individual test case
    def setUp(self):
        super().setUp()
        print('\nIn setUp()')
        # tearDown methods may not all be invoked if there are errors in the
        # process of cleaning up fixtures. To ensure that a fixture is always
        # released correctly, use addCleanup()
        # self.addCleanup(remove_tmpdir, self.tmpdir)

    def tearDown(self):
        super().tearDown()
        print('In tearDown()')


    # Assertions
    def test_fail(self):
        "self.fail('AssertionError')"

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_equal(self):
        self.assertEqual(2, 2, msg='failure message')

    def test_not_equal(self):
        self.assertNotEqual(3, 7, msg='failure message')

    def test_almost_equal(self):
        # self.assertEqual(1.1, 3.3 - 2.2)
        self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)            # number of decimal places to use for the test

    def test_almost_not_equal(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)


    # Containers
    def test_in(self):
        self.assertIn(3, {1: '1', 3: '3'})

    def test_not_in(self):
        self.assertNotIn(4, set([1, 2, 3]))

    def test_dict(self):
        # assertListEqual, assertSetEqual, assertTupleEqual, assertSequenceEqual
        # self.assertDictEqual({'a': 1, 'b': 2}, {'a': 1, 'b': 3})
        self.assertDictEqual(
            {'a': 1, 'b': 2},
            {'a': 1, 'b': 2},
        )

    def test_count(self):
        # self.assertCountEqual([1, 2, 3, 2], [1, 3, 2, 3])
        self.assertCountEqual(
            [1, 2, 3, 2],
            [1, 2, 3, 2],
        )


    # Exceptions
    def test_exception(self):
        # self.assertRaises(TypeError, shuffle, (1, 2, 3))
        with self.assertRaises(TypeError, msg='failure message'):
            shuffle((1, 2, 3))


    # SubTest - Repeating Tests with Different Inputs
    def test_with_subtest(self):
        for pat in ['a', 'B', 'c', 'd']:
            with self.subTest(pattern=pat):
                self.assertRegex('abc', pat)


    # Skipping Tests
    @unittest.skip('always skipped')
    def test_skip(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2, 'only runs on python 2')
    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == 'Darwin', 'only runs on macOS')
    def test_macos_only(self):
        self.assertTrue(True)

    def test_raise_skiptest(self):
        raise unittest.SkipTest('skipping via exception')


    # Ignoring Failing Tests
    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)

    # If a test that is expected to fail does in fact pass, that condition is
    # treated as a special sort of failure and reported as an “unexpected success”
    @unittest.expectedFailure
    def test_always_passes(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)










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










# Mocks (Imitacje, atrapy, fałszywe obiekty) - tworzenie fikcyjnej implementacji API

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
coverage html --omit '*/Ve-HomePage/*'



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
6. Try to not create database instances(no save()), try to focuse on full_clean()



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



# Other Libraries:
1. py.test (wydajność, elastyczny i wyjątkowo łatwy sposób zarządzania kontekstem wykonania testów,
    możliwosć rozproszenia testów na wiele komputerów)
2. nose
3. doctest (pewne testy dokumentacyjne są bardzo nieczytelne)
4. factory_boy(fixtures)





# PyTest

# implementacja kontekstu dla testów

import pytest

@pytest.fixture()
def prime_numbers():
    """Dostarcza kontekst zawierający liczby pierwsze"""
    return [3, 5, 7]

@pytest.fixture()
def non_prime_numbers():
    """Dostarcza kontekst zawierający liczby złożone"""
    return [8, 0, 1]

@pytest.fixture()
def negative_numbers():
    """Dostarcza kontekst zawierający liczby ujemne"""
    return [-1, -3, -6]


def test_is_prime_true(prime_numbers):
    """Sprawdż, czy funkcja is_prime() zwraca wartość
    True dla liczb pierwszych"""
    for number in prime_numbers:
        assert is_prime(number)

def test_is_prime_false(non_prime_numbers, negative_numbers):
    ...





# deazaktywacja wybranych testów i klas testowych

@pytest.mark.skipif(
    sys.platform == 'win32',
    reason='Niewspierane środowisko Windows'
)
class TestPosixCalls:
    def test_function(self):
        """Ten test nie powinien być uruchomiony w środowisku Windows"""


# wcześniejsza definicja warunków pomijania testów, łatwe współdzielenie między testami
skip_windows = pytest.mark.skipif(
    sys.platform == 'win32',
    reason='Niewspierane środowisko Windows'
)

@skip_windows
class TestPosixCalls:
    def test_function(self):
        """Ten test nie powinien być uruchomiony w środowisku Windows"""



# testy które w konkretnych warunkach powinny zakończyć się niepowodzeniem
# test zawsze bedzie wykonany, jednakże w określonych warunkach oczekiwana będzie porażka, a nie sukces
@pytest.mark.xfail(
    sys.platform == 'win32',
    reason='Niewspierane środowisko Windows'
)
class TestPosixCalls:
    def test_function(self):
        """Ten test musi zakończyć się niepowodzeniem w środowisku Windows"""





# fałszywe obiekty zastępcze i atrapy
# monkey-patching - dynamicznie zmodyfikować oprogramowanie w czasie uruchomienia, bez modyfikacji kodu źródłowego

# Fakes (fałszywe obiekty)
import smtplib
import pytest
from mailer import send

class FakeSMTP(object):
    def __init__(self, *args, **kwargs):
        pass
    def quit(self):
        pass
    def sendmail(self, *args, **kwargs):
        return {}

@pytest.yield_fixture()
# dekorator pozwalający na zarządzanie kontekstem wykonania testu za pomocą składni generatorów
def patch_smtplib():
    old_smtp = smtplib.SMTP
    smtplib.SMTP = FakeSMTP

    yield
    # zakopńczenie kontekstu: przywróć zawartość modułu do poprzedniego stanu
    smtplib.SMTP = old_smtp

def test_send(patch_smtplib):
    # function send uses 'server = smtplib.SMTP(server)'
    res = send(...)
    assert res == {}



# używając wbudowanego zarządcę kontekstu narzędzia py.test, monkeypatch
class FakeSMTP(object):
    def __init__(self, *args, **kwargs):
        pass
    def quit(self):
        pass
    def sendmail(self, *args, **kwargs):
        return {}

def test_send(monkeypatch):
    monkeypatch.setattr(smtplib, 'SMTP', FakeSMTP)

    res = send(...)
    assert res = {}



# Mocks (atrapy)
import smtplib
from unittest.mock import MagicMock
from mailer import send

def test_send(monkeypatch):
    smpt_mock = MagicMock()
    smpt_mock.sendmail.return_value = {}

    monkeypatch.setattr(smtplib, 'SMTP', MagicMock(return_value=smpt_mock))

    res = send(...)
    assert res == {}

# or
from unittest.mock import patch
from mailer import send

def test_send(monkeypatch):
    with patch('smtp.SMTP') as mock:
        instance = mock.return_value
        instance.sendmail.return_value = {}

        res = send(...)
        assert res == {}
