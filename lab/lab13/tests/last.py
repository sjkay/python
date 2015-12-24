test = {
  'name': 'last',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (last (list 1 2 3))
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (last (list 'a 'b 'c 'd 'e 'f))
          f
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (last '(1))
          1
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