## Interfaces ##

# Q1
class MixedJuiceVendor(object):
    """ A QueueVendingMachine that vends mixed juices. 

    >>> vendor = MixedJuiceVendor(['kiwi', 'mango', 'apple', 'guava'], 3)
    >>> juice = vendor.dispense()
    >>> juice
    'kiwi-mango'
    >>> vendor.collect_money(juice)
    9
    >>> juice = vendor.dispense()
    >>> juice
    'apple-guava'
    >>> vendor.collect_money(juice)
    19
    >>> vendor.cups
    1
    >>> juice = vendor.dispense() # no fruits left!
    >>> print(juice)
    None
    
    >>> vendor2 = MixedJuiceVendor(['guava', 'mango'], 0)
    >>> juice = vendor2.dispense() # no cups!
    >>> print(juice)
    None

    >>> vendor3 = MixedJuiceVendor(['lemon'], 1)
    >>> juice = vendor3.dispense() # only one fruit!
    >>> print(juice)
    None
    """

    def __init__(self, fruits, cups):
        """ fruits is a list of fruits in the inventory. cups is the number of 
            cups left to put juice in. 
        """
        self.fruits = fruits
        self.cups = cups
        self.revenue = 0

    def dispense(self):
        """ Dispenses a mixed juice combining the first two fruits in the 
            fruit inventory. Juices can only be created if there are at least 
            two fruits left and there is at least one cup left. 
        """
        "*** YOUR CODE HERE ***"

    def collect_money(self, item):
        """ Each juice is priced based on how many letters make up its two 
            fruits.
        """
        "*** YOUR CODE HERE ***"

# Q2
def total_revenue(qvm):
    """ Returns total possible revenue generated from qvm.
    
    >>> juices = MixedJuiceVendor(['orange', 'mango', 'banana', 'guava'], 10)
    >>> total_revenue(juices)
    22
    >>> snacks = SnacksVendor(['chips', 'ramen', 'pretzels', 'chips'], 
    ...                       {'chips': 4, 'pretzels': 7, 'ramen': 10})
    >>> total_revenue(snacks)
    25
    """
    "*** YOUR CODE HERE ***"

# Q3
def max_revenue(lst_of_qvm):
    """ Returns the QueueVendingMachine from lst_of_qvm that has the greatest 
        total possible revenue, or the first in the list if their total 
        revenues are equal.
    
    >>> juices = MixedJuiceVendor(['orange', 'mango', 'banana', 'guava'], 10)
    >>> snacks = SnacksVendor(['chips', 'ramen', 'pretzels', 'chips'], 
    ...     {'chips': 4, 'pretzels': 7, 'ramen': 10})
    >>> best = max_revenue([juices, snacks])
    >>> best is snacks
    True
    """
    "*** YOUR CODE HERE ***"

# SnacksVendor
class SnacksVendor(object):
    
    def __init__(self, snacks, prices):
        """ snacks is a list of all the snacks (strings) for sale, and can 
            contain multiple instances of the same snack type. prices is a 
            dictionary that maps each snack type (string) to its price (number)
            .
        """
        self.inventory = snacks
        self.prices = prices
        self.revenue = 0

    def dispense(self):
        """ Removes and dispenses the last snack from the inventory.

        >>> vendor = SnacksVendor(['candy', 'chips', 'chips'], 
        ...                       {'candy': 1, 'chips': 3})
        >>> vendor.dispense()
        'chips'
        >>> vendor.dispense()
        'chips'     
        >>> vendor.dispense()
        'candy'     
        >>> no_snack_left = vendor.dispense()
        >>> no_snack_left is None
        True
        """
        if self.inventory:
            return self.inventory.pop()

    def collect_money(self, item):
        """ Adds the price of snack to total revenue and returns the total 
            revenue.

        >>> vendor = SnacksVendor(['candy', 'chips'], {'candy': 1, 'chips': 3})
        >>> snack = vendor.dispense()
        >>> vendor.collect_money(snack)
        3
        >>> vendor.collect_money(vendor.dispense())
        4
        """
        self.revenue += self.prices[item]
        return self.revenue

## Magic Methods ##

# Q4
def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence 
    that reads the same forwards as backwards
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    "*** YOUR CODE HERE ***"


# Q5
class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __mul__(self, c):
        """ Scalar multiplies self by c. Raise AssertionError if c is not a 
            number.
        >>> (Link.empty * 3) is Link.empty
        True
        >>> a = Link(1, Link(5))
        >>> b = a * 1
        >>> b
        Link(1, Link(5))
        >>> b is not a
        True
        >>> b = a * 3
        >>> b
        Link(1, Link(5, Link(1, Link(5, Link(1, Link(5))))))
        >>> a is not b
        True
        >>> (a * 0) is Link.empty
        True
        >>> a * Link(3)
        AssertionError
        """
        "*** YOUR CODE HERE ***"

# Q6
def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception' and
    map it to the string 'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    >>> d[4]
    'no value'
    """
    "*** YOUR CODE HERE ***"

