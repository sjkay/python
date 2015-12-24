test = {
  'name': 'fibs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define fibs (make-fib-stream 0 1))
          fibs
          scm> (stream-to-list fibs 10)
          (0 1 1 2 3 5 8 13 21 34)
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