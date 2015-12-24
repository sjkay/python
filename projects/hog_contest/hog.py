"""This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry."""
	
def is_swap(score0, score1):
    def split(score):
        return (score // 10) % 10, score % 10
    score0_1, score0_2 = split(score0)
    score1_1, score1_2 = split(score1)
    if score0_1 == score1_2 and score0_2 == score1_1:
        return True
    else:
        return False

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    digit1, digit2 = opponent_score // 10, opponent_score % 10
    if max(digit1, digit2) + 1 >= margin :
        return 0
    else :
        return num_rolls 

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    digit1, digit2 = opponent_score // 10, opponent_score % 10
    add_score = max(digit1, digit2) + 1
    if is_swap(score + add_score, opponent_score):
        if (score + add_score) < opponent_score:
            return 0
        elif (score + add_score) == opponent_score:
            if add_score >= margin:
                return 0
            else:
                return num_rolls
        else :
            return num_rolls
    else :
        return bacon_strategy(score, opponent_score, margin, num_rolls)

def final_strategy(score, opponent_score):
    digit1, digit2 = opponent_score // 10, opponent_score % 10     
    if score + max(digit1, digit2) >= 99:
        return 0
    if score + max(digit1, digit2) > 89 and score + max(digit1, digit2) < 95:
        return 0
    if score > 88:
        return 1
    if score < 2:
        return 8
                                           
    if score - opponent_score > 51 :
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
    else:
        return swap_strategy(score,opponent_score,11,6)

