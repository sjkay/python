## Interfaces Extra ##

# Q7
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

    def __delitem__(self, index):
        """ Deletes value at given index from the Link. Raise a ValueError if the 
        length of the Linked List is 1. Raise an IndexError if the index is out
        of bounds.

        >>> s = Link(2, Link(4, Link(6, Link(8))))
        >>> del s[3]
        >>> s
        Link(2, Link(4, Link(6)))        
        >>> del s[4]
        Traceback (most recent call last):
             ...
        IndexError
        >>> del s[0]
        >>> s
        Link(4, Link(6))
        >>> del s[0]
        >>> s
        Link(6)
        >>> del s[0]
        Traceback (most recent call last):
             ...
        ValueError
        """
        "*** YOUR CODE HERE ***"
