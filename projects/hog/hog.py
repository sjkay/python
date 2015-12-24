"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    total, pigout = 0, 0
    while num_rolls > 0:
        current_roll = dice()
        if current_roll == 1:
            pigout = 1  
        else: 
            total += current_roll
        num_rolls -=1
    if pigout:    
        return pigout
    return total 
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    digit1, digit2 = opponent_score // 10, opponent_score % 10
    if num_rolls==0:
        return max(digit1, digit2) + 1
    return roll_dice(num_rolls,dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7:
        return six_sided
    return four_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    def split(score):
        """ Return tenth digit and one digit
        """
        return (score // 10) % 10, score % 10
    score0_1, score0_2 = split(score0)
    score1_1, score1_2 = split(score1)
    if score0_1 == score1_2 and score0_2 == score1_1:
        return True
    return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0,score1), score1, select_dice(score0,score1))
        else :
            score1 += take_turn(strategy1(score1,score0), score0, select_dice(score1,score0))     
        if is_swap(score0,score1): 
            score0, score1 = score1, score0
        who = other(who)
    # END Question 5
    return score0, score1

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    # BEGIN Question 6
    def return_average(*args):
        count, total = 0, 0
        while count < num_samples:
            count += 1
            total += fn(*args)
        return total / num_samples
    return return_average
    # END Question 6

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    i_roll, max_score = 1, 0
    while i_roll <=10:
        i_score = make_averaged(roll_dice)(i_roll,dice)
        if max_score < i_score:
           max_score, best_i = i_score, i_roll
        i_roll += 1
    return best_i
    # END Question 7

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))


    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    digit1, digit2 = opponent_score // 10, opponent_score % 10
    if max(digit1, digit2) + 1 >= margin :
        return 0
    return num_rolls 
    # END Question 8

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS if rolling 0 dice results in a harmful swap. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    # BEGIN Question 9
    digit1, digit2 = opponent_score // 10, opponent_score % 10
    add_score = max(digit1, digit2) + 1
    if is_swap(score + add_score, opponent_score):
        if (score + add_score) < opponent_score:
            return 0
        elif (score + add_score) == opponent_score:
            if add_score >= margin:
                return 0
            return num_rolls
        return num_rolls
    return bacon_strategy(score, opponent_score, margin, num_rolls)
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    first, make sure when a move can make me win, i would always go for it.
    ***(the next was found by random and just testing out the rolls. not too sure why it works best for the threshold. returning 0 is advantageous in those conditions)
    ***I also added a threshold where one roll would give a higher percentage as i dont need to take risk when im close to 100 (lowest risk)
    ***And also added a threshold for the opposite case when high risk can be taken. 8 rolls when score is less than 2 was optimal.
    following the advice about risks, i will have less num_rolls if im leading (less risk)
    if im losing i will take more risk and and increase my num_rolls
    margin will also work in the same principle as as num_rolls
    keep tweaking and adding bounds so percentage gets higher until satisfied.
	***Note: the *** were done at the end as i was playing around and tweaking. doing these first may not be a good idea as they override the boundaries that come after
    """
    # BEGIN Question 10
    digit1, digit2 = opponent_score // 10, opponent_score % 10     
    if score + max(digit1, digit2) >= 99:
        return 0
    elif score + max(digit1, digit2) > 89 and score + max(digit1, digit2) < 95:
        return 0
    elif score > 88:
        return 1
    elif score < 2:
        return 8
    elif score - opponent_score > 51 :
        return swap_strategy(score,opponent_score,4,1)
    elif score - opponent_score > 40 :
        return swap_strategy(score,opponent_score,5,3)
    elif score - opponent_score > 30 : 
        return swap_strategy(score,opponent_score,5,4)
    elif score - opponent_score > 25 :
        return swap_strategy(score,opponent_score,6,4)
    elif score - opponent_score > 16 :
        return swap_strategy(score,opponent_score,6,5)
    elif score > opponent_score:
        return swap_strategy(score,opponent_score,7,5)
    elif opponent_score - score > 24:
        return swap_strategy(score,opponent_score,11,10)
    elif opponent_score - score > 17:
        return swap_strategy(score,opponent_score,11,8)
    elif opponent_score - score > 14:
        return swap_strategy(score,opponent_score,11,7)
    return swap_strategy(score,opponent_score,11,6)
    # END Question 10


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--final', action='store_true',
                        help='Display the final_strategy win rate against always_roll(5)')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
    elif args.final:
        from hog_eval import final_win_rate
        win_rate = final_win_rate()
        print('Your final_strategy win rate is')
        print('    ', win_rate)
        print('(or {}%)'.format(round(win_rate * 100, 2)))
