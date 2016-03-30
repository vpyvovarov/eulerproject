from unittest import TestCase
import problem as mud


class Test(TestCase):

    def _check_get_primes(self, number, expected_result):
        """ Verify that list of prime number generator work correct"""
        result = mud.get_primes(number)
        diff = set(result).symmetric_difference(set(expected_result))
        error_msg = "list of primes \n %s \n is incorrect should be \n%s\n. Difference: %s" %\
                    (result, expected_result, diff)
        self.assertFalse(diff, error_msg)

    def _check_is_prime(self, number, is_prime):
        """ Verify that prime numbers detection work correct"""
        result = mud.is_prime(number)
        error_msg = "number %s should be %s" % (number, "prime" if is_prime else "not prime")
        self.assertTrue(result == is_prime, error_msg)

    def test_is_prime_positive(self):
        """ Positive test for is_prime function"""
        dataset = (1, 3, 5, 7, 11, 13, 41)
        for number in dataset:
            self._check_is_prime(number, True)

    def test_is_prime_negative(self):
        """ Negative test for is_prime function"""
        dataset = (4, 6, 8, 9, 10, 64)
        for number in dataset:
            self._check_is_prime(number, False)

    def test_get_primes_positive(self):
        """ Positive test for get_primes function"""
        dataset = {10:  (2, 3, 5, 7),
                   100: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97),
                   200: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                         197, 199)}
        for number, expected in dataset.iteritems():
            self._check_get_primes(number, expected)

    def test_calc_longest(self):
        """ Positive test for calc_longest function"""
        dataset = {41:  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97),
                   197: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                         197, 199)}
        for expected, primes in dataset.iteritems():
            result = mud.calc_longest(primes)
            self.assertTrue(result == expected, "For %s longest chain is %s, instead got %s" %
                            (primes, expected, result))
