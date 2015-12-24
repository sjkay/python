################
# Lab 7: Trees #
################

def lab7_q1():
    """
    >>> isinstance(lab7_q1(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab7_q2():
    """
    >>> isinstance(lab7_q2(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab7_q3():
    """
    >>> isinstance(lab7_q3(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab7_q4():
    """
    >>> isinstance(lab7_q4(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

######################################
# Lab 8: Object-Oriented Programming #
######################################

def lab8_q2():
    """
    >>> isinstance(lab8_q2(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab8_q3():
    """
    >>> isinstance(lab8_q3(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab8_q4():
    """
    >>> isinstance(lab8_q4(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab8_q5():
    """
    >>> isinstance(lab8_q5(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

###############################
# Lab 9: Mutable Linked Lists #
###############################

def lab9_q2():
    """
    >>> isinstance(lab9_q2(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab9_q3():
    """
    >>> isinstance(lab9_q3(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab9_q4():
    """
    >>> isinstance(lab9_q4(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

def lab9_q5():
    """
    >>> isinstance(lab9_q5(), str)
    True
    """
    return """
    YOUR EXPLANATION HERE
    """

######################
# Lab 10: Interfaces #
######################

def lab10_q1():
    """
    >>> isinstance(lab10_q2(), str)
    True
    """
    return """
    Since there has to be at least two, len(self.fruits) >=2 and at least one cup, self.cups (number == True)
	Decrease cups by 1 because we use one to create mixed juice.
	first pop gives the 0 index fruit, second pop gives the next 0 index which is originally at 1 index.
	
	len(item) to show number of letters then -1 because of hyphen.
    """

def lab10_q2():
    """
    >>> isinstance(lab10_q3(), str)
    True
    """
    return """
    Make a 'total' to add up the total revenue as while loop plays.
	item = qvm.dispense, makes it so item is the juice. 
	While item: because if there is a juice this while loop will continue. If there aren't two fruits, there wont be a juice so while loop stops.
	total += qvm.collect_money(item). (this should be += not = right?) to add the revenue from that 'item'
	revalue item to the next juice.
	return total
    """

def lab10_q3():
    """
    >>> isinstance(lab10_q4(), str)
    True
    """
    return """
    Use list comprehension max(lst_of_qvm, key=lambda qvm : total_revenue(qvm))
	This makes each element of the list go through the key which gives total_revenue for each one. Then just get the max in that list
    """

def lab10_q4():
    """
    >>> isinstance(lab10_q5(), str)
    True
    """
    return """
    Use 'for i in range(len(seq)//2):' to give i be the indexing for the first half of the lst.
    Then make sure it is equal to the opposite indexing which is [-i-1] or [len(seq)-1-i]
	if it is not equal return false
	if the for loop is done without fail it means they are all equal so return True
    """

def lab10_q5():
    """
    >>> isinstance(lab10_q5(), str)
    True
    """
    return """
    'assert type(c) is int' to make sure c is a number/integer
	make a helper function to solve this with the same parameters
	first base case is if the count is 0 which returns Link.empty if true
	Then is when lst is Link.empty, which should just Link.empty as well
	recursion for these base cases  where you just link the first with the helper(rest, c) :Link(lst.first, helper(lst.rest, count))
    """

def lab10_q6():
    """
    >>> isinstance(lab10_q5(), str)
    True
    """
    return """
    Use try: return dictionary[key] so that if there is a key and value the value will be the output.
	make except Keyerror where it prints "Avoid Exception" and the new value for this key will be 'no value' next time it is called. It will output 'no value'
    """
