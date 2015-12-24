test = {
  'name': 'reverse',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (reverse (list 1 2 3))
          (3 2 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (reverse (list 'a 'b 'c 'd 'e 'f))
          (f e d c b a)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (reverse '(1))
          (1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (reverse '())
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}