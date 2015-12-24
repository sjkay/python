test = {
  'name': 'What would Scheme print?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define ones (cons-stream 1 ones))
          ones
          scm> (define twos (cons-stream 2 twos))
          twos
          scm> (has-even? twos)
          True
          scm> (define (foo x) (+ x 1))
          foo
          scm> (define bar (cons-stream (foo 1) (cons-stream (foo 2) bar)))
          bar
          scm> (car bar)
          2
          scm> (define (foo x) (+ x 5))
          foo
          scm> (car bar)
          2
          scm> (stream-cdr bar)
          (7 . #[promise (not forced)])
          scm> (define (foo x) (+ x 7))
          foo
          scm> (stream-cdr bar)
          (7 . #[promise (not forced)])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define (has-even? s)
      ....   (cond ((null? s) False)
      ....         ((even? (car s)) True)
      ....         (else (has-even? (stream-cdr s)))))
      has-even?
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}