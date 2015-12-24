test = {
  'name': '__mul__',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab10 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}