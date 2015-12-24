test = {
  'name': '__delitem__',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = Link(2, Link(4, Link(6, Link(8))))
          >>> del s[3]
          >>> s
          Link(2, Link(4, Link(6)))
          >>> del s[4]
          IndexError
          >>> del s[0]
          >>> s
          Link(4, Link(6))
          >>> del s[0]
          >>> s
          Link(6)
          >>> del s[0]
          ValueError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab10_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}