test = {
  'name': 'stream-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a (cons-stream 1 (cons-stream 2 (cons-stream 3 nil))))
          a
          scm> (stream-to-list (stream-filter a even?) 10)
          (2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define a (cons-stream 3 (cons-stream 6 (cons-stream 8 (cons-stream 4 (cons-stream 5 (cons-stream 3 nil)))))))
          a
          scm> (stream-to-list (stream-filter a odd?) 10)
          (3 5 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define both (cons-stream 1 (cons-stream 2 both)))
          both
          scm> (stream-to-list (stream-filter both even?) 10)
          (2 2 2 2 2 2 2 2 2 2)
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