test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          403f02fd254a4c6524542453898124b4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two add-one) 2)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          403f02fd254a4c6524542453898124b4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab11)
      scm> (define (add-one a) (+ a 1))
      scm> (define (multiply-by-two a) (* a 2))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}