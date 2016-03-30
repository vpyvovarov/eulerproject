from unittest import TestCase
import problem as mud


class Test(TestCase):

    def _check_make_reverse(self, dataset, as_str):
        """ Verify that make_reverse function work correct or raise error if not"""
        for number, expected in dataset.iteritems():
            result = mud.make_revers(number, as_str=as_str)
            _str = "As string." if as_str else ""
            self.assertTrue(result == expected, "Reversed number problem. %s Expected %s, got %s" %
                            (_str, expected, result))

    def _check_is_palindromic(self, dataset):
        """ Verify that is_palindromic function work correct or raise error if not"""
        for number, expected in dataset.iteritems():
            result = mud.is_palindromic(number)
            expected_str = "palindromic" if expected else "not palindromic"
            result_str = "palindromic" if result else "not palindromic"
            self.assertTrue(result == expected, "number %s expected to be %s, but detected as %s instead" %
                            (number, expected_str, result_str))

    def test_make_revers(self):
        """ Test for make_revers function. Return result is integer"""
        dataset = {121: 121,
                   501: 105,
                   100: 1,
                   7:   7}
        self._check_make_reverse(dataset, as_str=False)

    def test_make_revers_str(self):
        """ Test for make_revers function. Return result is string"""
        dataset = {121: '121',
                   501: '105',
                   100: '001',
                   7:   '7'}
        self._check_make_reverse(dataset, as_str=True)

    def test_is_palindromic_positive(self):
        """ Positive test is_palindromic function."""
        dataset = {121:  True,
                   555:  True,
                   8998: True,
                   7:    True}
        self._check_is_palindromic(dataset)

    def test_is_palindromic_negative(self):
        """ Negative test is_palindromic function."""
        dataset = {500:  False,
                   13:   False,
                   9090: False,
                   7878: False}
        self._check_is_palindromic(dataset)

    def test_revers_and_process(self):
        """ Test revers_and_process function."""
        dataset = {47:   121,
                   349:  1292,
                   1292: 4213,
                   4213: 7337}
        for number, expected in dataset.iteritems():
            result = mud.revers_and_process(number)
            self.assertTrue(expected == result, "reverse_and_precess return incorrect result. Expected %s, got %s" %
                            (expected, result))

    def test_check_number(self):
        """ Test check_number function."""
        dataset = {(47, 1):     True,
                   (47, 10):    True,
                   (349, 10):   True,
                   (349, 2):    False,
                   (196, 50):   False,
                   (196, 12):   False,
                   (10677, 50): False,
                   (10677, 54): True}
        for parametes, expected in dataset.iteritems():
            number, iterations = parametes
            result = mud.check_number(number, iterations)
            self.assertTrue(expected == result,
                            "check_number return incorrect result for %s, number of iterations %s. Expected %s, got %s" %
                            (number, iterations,  expected, result))
