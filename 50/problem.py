# https://projecteuler.net/problem=50
import time
from math import sqrt


def is_prime(number):
    """ Check if number is prime """
    for divider in xrange(2, int(sqrt(number)) + 1):
        if not number % divider:
            return False
    return True


def get_primes(r=100):
    """ Get list of prime numbers less then r"""
    return filter(is_prime, xrange(2, r))


def calc_longest(primes):
    """ From list of ordered primes calc longest chain of primes sum of which is prime number"""
    primes_sum = sum(primes)
    result = {}
    start = 0
    end = len(primes) - 1

    # have to iterate though max_prime separately
    max_prime_index = len(primes) - 1
    max_prime = primes[max_prime_index]
    while start < end and max_prime_index:

        # to not sum across list of primes remember the value and reduce sum at the end
        out = 0

        # could remove max value. This should be first because we need longest chain
        if primes_sum - primes[end] >= max_prime:
            out = primes[end]
            end -= 1

        # could remove lowest value
        elif primes_sum - primes[start] >= max_prime:
            out = primes[start]
            start += 1

        # current max_prime could not be form as sum of primes
        else:

            # remove from list of primes max value
            start = 0
            primes_sum = sum(primes[:end])

            # get next max prime
            max_prime_index -= 1
            max_prime = primes[max_prime_index]

        # get new sum
        primes_sum = primes_sum - out

        if primes_sum == max_prime:

            # get chain
            result[end-start] = max_prime
            end -= 1
    # find longest chain
    key = max(result)
    return result[key]

if __name__ == "__main__":
    start_time = time.time()
    p = get_primes(1000)
    print calc_longest(p)
    end_time = time.time()
    print "in %s" % (end_time - start_time)
