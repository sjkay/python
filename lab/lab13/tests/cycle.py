test = {
  'name': 'cycle',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cycle nil)
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (stream-to-list (cycle '(1)) 10)
          (1 1 1 1 1 1 1 1 1 1)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (stream-to-list (cycle '(1 2 3)) 10)
          (1 2 3 1 2 3 1 2 3 1)
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