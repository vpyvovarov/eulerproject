# https://projecteuler.net/problem=55
import time


def make_revers(number, as_str=True):
    """ Reverse order of digit in number"""
    str_list = list(str(number))
    str_list.reverse()
    result = "".join(str_list)
    if as_str:
        return result
    return int(result)


def revers_and_process(number):
    """ Perform one iteration of Algorithm"""
    rev = make_revers(number, as_str=False)
    return rev + number


def is_palindromic(number):
    """ Check if given number is palindromic"""
    str_reversed = make_revers(number)
    return str_reversed == str(number)


def check_number(number, iterations=49):
    """ Check if we could produce palindromic number is given steps of iterations"""
    for _ in xrange(iterations):
        number = revers_and_process(number)
        if is_palindromic(number):
            return True
    return False


if __name__ == "__main__":
    start = time.time()
    count = 0
    for i in xrange(10000):
        if not check_number(i):
            count += 1
    print count
    end = time.time()
    print "in %s" % (end - start)
