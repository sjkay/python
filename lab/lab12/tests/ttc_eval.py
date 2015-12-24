test = {
  'name': 'ttc_eval',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '87dbaa4c3e856d184556f0af018ad4f4',
          'choices': [
            'in_game_parse',
            'end_game_parse',
            'new_game',
            'in_game_parse and end_game_parse'
          ],
          'hidden': False,
          'locked': True,
          'question': 'ttc_eval takes in output from which function(s)?'
        },
        {
          'answer': '616bf67c14406c0aa1d74e7a5badf706',
          'choices': [
            'ttc_apply',
            'in_game_parse',
            'end_game_parse'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What function must be called in ttc_eval?'
        },
        {
          'answer': '5755dbc79c6ab1ce10465974d0750d29',
          'choices': [
            'Reset',
            'NewGame',
            'New'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following is not a command a player can input?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> b = Board(False) # Create a board that doesn't print unnecessarily
          >>> line = "Place X at 7"
          >>> exp = in_game_parse(line)
          >>> ttc_eval(b, exp)
          'X has been placed in space 7'
          >>> ttc_eval(b, in_game_parse("O in for 6"))
          'O has been placed in space 6'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from interpreter import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}