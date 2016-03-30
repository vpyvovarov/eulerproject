import problem as mud
from unittest import TestCase


@mud.caching_decorator
def _simple_func(a, b, c=1, d=2):
    return a, b, c, d


class Test(TestCase):

    def _verify_decorated_result(self, expected, args, result):
        """ Compare two values and raise error if they are different """
        self.assertTrue(result == expected, "caching decorator spoil function. Arguments %s. Expected %s, got %s" %
                        (args, expected, result))

    def test_calc(self):
        """ Test that function calc produce correct results"""
        dataset = {(3, 7):  17,
                   (3, 40): 133957148,
                   (3, 50): 16475640049}
        for args, expected in dataset.iteritems():
            min_tile_size, field_size = args
            result = mud.calc(min_tile_size, field_size)
            self.assertTrue(result == expected,
                            "calc function work incorrectly. Arguments: %s, %s. Expected %s, got %s" %
                            (min_tile_size, field_size, expected, result))

    def test_caching_decorator_functional(self):
        """Test that caching decorator doesn't spoil function result"""
        dataset = [(1, 2, 3, 4), ('1', '2', '3', '4'), ('4', '3', '2', '1'), (4, 3, 2, 1), ('a', 'a', 1, 1)]

        dec_func = mud.caching_decorator(_simple_func)
        for args in dataset:
            a, b, c, d = args
            result = dec_func(a, b, c, d)
            self._verify_decorated_result(args, args, result)

    def test_caching_decorator_default_args(self):
        """Test that caching decorator doesn't spoil default arguments"""
        dec_func = mud.caching_decorator(_simple_func)

        result = dec_func(1, 2,)
        self._verify_decorated_result((1, 2, 1, 2), (1, 2), result)
