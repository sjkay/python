class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __contains__(self, value):
        "*** YOUR CODE HERE ***"
        if self == Link.empty:
            return False
        elif self.first == value:
            return True
        else:
            return value in self.rest

class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]

    >>> m = ScaleIterator(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        "*** YOUR CODE HERE ***"
        self.i = 0
        self.s = iter(elem*k for elem in s)

    def __iter__(self):
        return self

    def __next__(self):
        "*** YOUR CODE HERE ***"
        return next(self.s)


def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
#    return (elem*k for elem in s)
    for s in s:
        yield s*k


def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"
#    result= []
#    try: 
#        while True:
#            if next(i0) < next(i1):
#                result.append(next(i0)
#            elif next(i0) == next(i1):
#                result.append(next(i0)
#                yield next(i1)
#            else:
#                result.append(next(i1)
    while True:
        if e0 < e1:
            yield e0
            e0 = next(i0)
        elif e0 > e1:
            yield e1
            e1 = next(i1)
        else:
            yield e0
            e0, e1 = next(i0), next(i1)


def make_s():
    """A generator function that yields all positive integers with only factors
    2, 3, and 5.

    >>> s = make_s()
    >>> type(s)
    <class 'generator'>
    >>> [next(s) for _ in range(20)]
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    "*** YOUR CODE HERE ***"
#    twos = scale(naturals(), 2)
#    threes = scale(naturals(), 3)
#    fives = scale(naturals(), 5)
#    twos_threes= merge(twos, threes)
#    return merge(twos_threes, fives)

#    i = 1
#    yield 1
#    while True:
#        i += 1
#        if i%2==0 or i%3==0 or i%5==0:
#            yield i

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    result = [1, 2, 3, 4, 5, 6]
    i = 7
    while True:
        if i/2 in result or i/3 in result or i/5 in result:
            result.append(i)
            yield i
        i += 1

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1. 

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


