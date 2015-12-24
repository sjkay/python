
better_keep_if = 1  # REPLACE None WITH 1 or 2

better_keep_if_explanation = """
YOUR EXPLANATION HERE
1 is shorter. 2 has redundant lines as code will do i+=1 regardless.
"""


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    i = 3
    a, b, c = 1, 2, 3   # c for current
    while i < n:
        a, b, c = b, c, 3*a + 2*b + c
        i += 1
    return c

from operator import add, sub
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
#    ans, count, add = 0, 1, 1
#    while count != n+1:
#        if has_seven(count) or count/7 == count//7:
#            ans, count, add = ans + add, count +1, add*-1
#        else:
#            ans, count = ans + add, count + 1
#    return ans
    def pp(value, dir, count):
        if count == n:
            return value
        if has_seven(count+1) or (count+1)%7==0:
            return pp(value + dir, -dir, count + 1)
        else:
            return pp(value + dir, dir, count + 1)
    return pp(1, 1, 1)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    coin = 1
    while 2*coin <= amount:
        coin = coin * 2

    def cc(money_now, coin_type):
        if money_now < 0:
            return 0
        elif money_now == 0:
            return 1
        elif coin_type == 1:
            return 1
        else:
            money_used = money_now - coin_type
            money_unused = money_now 
        
        return cc(money_used, coin_type) + cc(money_unused, coin_type/2) 

    return cc(amount, coin)


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    offset = 6 - start - end
    def move_disk(start, end):
        print("Move the top disk from rod", start, "to rod", end)
    if n == 1:
        move_disk(start,end)
#    elif n == 2:
#        move_disk(start, offset)
#        move_disk(start, end)
#        move_disk(offset, end)
    else:
#        if n/2 == n//2:
#            return towers_of_hanoi(n-1, start, offset), towers_of_hanoi(n-1, start, end)
#        else:
#            return towers_of_hanoi(n-1, start, end), towers_of_hanoi(n-1, start, offset)
       	towers_of_hanoi(n-1, start, offset)
        move_disk(start, end)
        towers_of_hanoi(n-1, offset, end)		

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'

