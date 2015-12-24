def is_sorted(lst):
    """Returns True if the linked list is sorted.

    >>> lst1 = link(1, link(2, link(3, link(4))))
    >>> is_sorted(lst1)
    True
    >>> lst2 = link(1, link(3, link(2, link(4, link(5)))))
    >>> is_sorted(lst2)
    False
    >>> lst3 = link(3, link(3, link(3)))
    >>> is_sorted(lst3)
    True
    """
    "*** YOUR CODE HERE ***"
    small = first(lst)
    lst = rest(lst)
    big = first(lst)
    lst = rest(lst)
    while lst != 'empty':
        if small > big:
            return False
        small, big, lst = big, first(lst), rest(lst)
    return True


def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    "*** YOUR CODE HERE ***"
    if s0 == 'empty' and s1 != 'empty':
        one, s1 = first(s1), rest(s1)
        return link(one, interleave(s0,s1))
    elif s0 != 'empty' and s1 == 'empty':
        one, s0 = first(s0), rest(s0)
        return link(one, interleave(s0,s1))
    elif s0 == 'empty' and s1 == 'empty':
        return 'empty'
    else: 
        one, two, s0, s1 = first(s0), first(s1), rest(s0), rest(s1)
        return link(one, link(two, interleave(s0,s1)))


def height(t):
    """Return the depth of the deepest node in the tree.

    >>> height(tree(1))
    0
    >>> height(tree(1, [tree(2), tree(3)]))
    1
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> height(numbers)
    2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    deepest = 0
    for subtree in subtrees(t):
        deepest = max(deepest, height(subtree))
    return deepest + 1


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
#    if is_leaf(t):
#        return tree(t, [tree(v) for v in vals])
#    else:
#        for subtree in t:
#            sprout_leaves(subtree, [tree(v) for v in vals])
    if is_leaf(t):
        return tree(entry(t), [tree(v) for v in vals])
    else:
        treerest = []
        for subtree in subtrees(t):
            treerest += [sprout_leaves(subtree, [tree(v) for v in vals])]
    return tree(entry(t), treerest)

###################
# Linked List ADT #
###################

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)


############
# Tree ADT #
############

import inspect
# Tree definition - same Data Abstraction but different implementation from lecture
def tree(entry, subtrees=[]):
    #for subtree in subtrees:
    # assert is_tree(subtree)
    return lambda dispatch: entry if dispatch == 'entry' else list(subtrees)

def entry(tree):
    return tree('entry')

def subtrees(tree):
    return tree('subtrees')

def is_tree(tree):
    try:
        tree_data = inspect.getargspec(tree)
        assert tree_data == inspect.getargspec(lambda dispatch: None)
        return all([is_tree(subtree) for subtree in subtrees(tree)])
    except:
        return False

def is_leaf(tree):
    return not subtrees(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(entry(t)))
    for subtree in subtrees(t):
        print_tree(subtree, indent + 1)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
