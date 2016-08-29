# UNIT TESTS

import unittest
class TestSomething(unittest.TestCase):
    def setUp(self):							       # initializations function for tests
	      self.nums = list(range(11))                  # When a setUp() method is defined, the test runner will run that
    def tearDown(self):                              # method prior to each test. Likewise, if a tearDown() method is
        ...                                          # defined, the test runner will invoke that method after each test.

    def test_numbers(self):                          # all methods will get run as the tests
        self.assertEqual(fun1(n), fun2(i), msg)      # if values are not equal it will throw an AssertionError
        self.assertTrue(element in self.nums, msg)   # to verify the condition
        self.assertRaises(                           # to verify that an expected exception gets raised
            TypeError, random.shuffle, (1, 2, 3))

    def test_sequence(self):
        ...

if __name__ == "__main__":
	unittest.main()
