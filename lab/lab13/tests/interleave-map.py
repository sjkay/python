test = {
  'name': 'interleave-map',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a (cons-stream 1 (cons-stream 3 (cons-stream 5 nil))))
          a
          scm> (define b (cons-stream 2 (cons-stream 4 (cons-stream 6 nil))))
          b
          scm> (stream-to-list (interleave-map a b) 10)
          (1 2 3 4 5 6)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define a (cons-stream 'a (cons-stream 'b (cons-stream 'c (cons-stream 'd (cons-stream 'e (cons-stream 'f nil)))))))
          a
          scm> (define b (cons-stream 1 (cons-stream 2 nil)))
          b
          scm> (stream-to-list (interleave-map a b) 10)
          (a 1 b 2 c)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define ones (cons-stream 1 ones))
          ones
          scm> (define twos (cons-stream 2 twos))
          twos
          scm> (stream-to-list (interleave-map ones twos) 10)
          (1 2 1 2 1 2 1 2 1 2)
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