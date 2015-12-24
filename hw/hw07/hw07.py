def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
#    if s.rest.rest == Link.empty:
#        s = Link(s.first)
#    else:
#        s.rest = every_other(s.rest.rest)
    def helper(s, counter):
        if counter < 3:
            s = Link(s.first)
        else:
            s.rest = every_other(s.rest.rest)
    return helper(s, len(s))


def has_cycle(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    "*** YOUR CODE HERE ***"
    temp = set()
    while s != Link.empty:
        if s in temp:
            return True
        temp.add(s)
        s = s.rest
    return False

def partial_tree(s, n):
    """Return a balanced tree of the first n elements of Link s, along with
    the rest of s. A tree is balanced if

      (a) the number of entries in its left branch differs from the number
          of entries in its right branch by at most 1, and

      (b) its non-empty branches are also balanced trees.

    Examples of balanced trees:

    BinaryTree(1)                                # branch difference 0 - 0 = 0
    BinaryTree(1, BinaryTree(2), None)           # branch difference 1 - 0 = 1
    BinaryTree(1, None, BinaryTree(2))           # branch difference 0 - 1 = -1
    BinaryTree(1, BinaryTree(2), BinaryTree(3))  # branch difference 1 - 1 = 0

    Examples of unbalanced trees:

    # branch difference 2 - 0 = 2
    BinaryTree(1, BinaryTree(2, BinaryTree(3)), None)
    # Unbalanced right branch
    BinaryTree(1, BinaryTree(2, BinaryTree(3), None),
            BinaryTree(4, BinaryTree(5, BinaryTree(6), None), None))

    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> partial_tree(s, 3)
    (BinaryTree(2, BinaryTree(1), BinaryTree(3)), Link(4, Link(5)))
    >>> t = Link(-2, Link(-1, Link(0, s)))
    >>> partial_tree(t, 7)[0]
    BinaryTree(1, BinaryTree(-1, BinaryTree(-2), BinaryTree(0)), BinaryTree(3, BinaryTree(2), BinaryTree(4)))
    >>> partial_tree(t, 7)[1]
    Link(5)
    """
    if n == 0:
        return BinaryTree.empty, s
    left_size = (n-1)//2
    right_size = n - left_size - 1
    "*** YOUR CODE HERE ***"
    left, rest = partial_tree(s, left_size)
    entry, rest = rest.first, rest.rest
    right, rest = partial_tree(rest, right_size)
    return BinaryTree(entry, left, right), rest

def ordered_sequence_to_tree(s):
    """Return a balanced tree containing the elements of ordered Link s.

    Note: this implementation is complete, but the definition of partial_tree
    above is not complete.

    >>> ordered_sequence_to_tree(Link(1, Link(2, Link(3))))
    BinaryTree(2, BinaryTree(1), BinaryTree(3))
    >>> elements = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7)))))))
    >>> ordered_sequence_to_tree(elements)
    BinaryTree(4, BinaryTree(2, BinaryTree(1), BinaryTree(3)), BinaryTree(6, BinaryTree(5), BinaryTree(7)))
    """
    return partial_tree(s, len(s))[0]


def has_cycle_constant(s):
    """Return whether Link s contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    return has_cycle(s)

##############################
# Linked List implementation #
##############################

class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

#############################
# BinaryTree implementation #
#############################

# Tree definition
class BinaryTree:
    empty = ()

    def __init__(self, entry, left=empty, right=empty):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == self.empty and self.right == self.empty:
            return 'BinaryTree({})'.format(repr(self.entry))
        left = 'BinaryTree.empty' if self.left == self.empty else self.left
        right = 'BinaryTree.empty' if self.right == self.empty else self.right
        return 'BinaryTree({}, {}, {})'.format(repr(self.entry),
                                               repr(left), repr(right))
