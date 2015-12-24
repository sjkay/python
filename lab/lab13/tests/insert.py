test = {
  'name': 'insert',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (insert 4 (list 1 2 3))
          (1 2 3 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (insert 4 (list 1 2 6 7))
          (1 2 4 6 7)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (insert 0 '(1))
          (0 1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}