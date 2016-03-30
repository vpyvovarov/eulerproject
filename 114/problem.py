# https://projecteuler.net/problem=114
import time
from functools import wraps


def caching_decorator(f):
    """ This decorator remember argument with which function was called and result of function execution
        If function will be called with the same parameters second time, instead of running function result
        will be returned from cache
    """
    results = {}

    @wraps(f)
    def wrapee(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in results:
            results[key] = f(*args, **kwargs)
        return results[key]
    return wrapee


@caching_decorator
def calc(min_tile_size, field_size):
    """ Calc number of ways row of size field_size could be filled with tiles of at least min_tile_size"""
    result = 1
    gape = 1
    if min_tile_size > field_size:
        # no more tails could be fitted
        return 1

    # how many units left
    for field_start in xrange(field_size - min_tile_size + 1):

        # different size of tiles
        for tile in xrange(min_tile_size, field_size - field_start+1):
            new_field_size = field_size - field_start - tile - gape
            result += calc(min_tile_size=min_tile_size, field_size=new_field_size)
    return result

if __name__ == "__main__":
    min_tile = 3
    size = 50
    start = time.time()
    print calc(min_tile_size=min_tile, field_size=size)
    end = time.time()
    print "in %s" % (end-start)
