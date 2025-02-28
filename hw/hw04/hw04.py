
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"
    if not lst:
        return 0
    elif type(lst[0]) == list:
        return deep_len(lst[0]) + deep_len(lst[1:])
    else:
        return 1 + deep_len(lst[1:])

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    if not lst:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return (a,b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return max(x)

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
    AssertionError
    """
    "*** YOUR CODE HERE ***"
    assert lower_bound(y)<=upper_bound(y)<0 or 0<lower_bound(y)<=upper_bound(y)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
# (1,2), (2,4)
# lots of intervals will give different results that show the interval for par2 to span less than par1.
# this is because when doing operatives with zero span (one = interval(1,1)) the range doesn't increase and par2 has only one operative that does.
# par1 has many operatives and the more operatives you use on intervals the range would get larger as there are more possible answers with a larger range. 

def multiple_references_explanation():
    return """The mulitple reference problem gives lots of intervals will give different results that show the interval for par2 to span less than par1. 
           This is because when doing operatives with zero span (one = interval(1,1)) the range doesn't increase and par2 has only one operative that does.
           par1 has many operatives and the more operatives you use on intervals the range would get larger as there are more possible answers with a larger range."""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(t):
        return a*t*t + b*t + c 
    ext, lower, upper = f(-b/(2*a)), f(lower_bound(x)), f(upper_bound(x))
    if lower_bound(x) <= -b/(2*a) < upper_bound(x):
        if a > 0:
            return interval(ext, max(lower,upper))
        else:
            return interval(min(lower,upper), ext)
    else:
        return interval(min(lower,upper), max(lower,upper))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    k = len(c)
    def f(t):
        a,f = 0, 0
        while a!=k:
            f = f + c[a]*pow(t,a)
            a+=1
        return f
    def deri(t):
        a,f = 0, 0
        while a!=k:
            f = f + (k-a-1)*c[a]*pow(t,a)
            a+=1
        return f
    guess = (lower_bound(x) + upper_bound(x))/2
    newton, lower, upper = -f(guess)/deri(guess) +guess, f(lower_bound(x)), f(upper_bound(x))
    if c[0] > 0:
        return interval(guess, max(lower,upper))
    else:
        return interval(min(lower,upper), guess)


