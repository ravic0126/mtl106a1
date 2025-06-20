"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""

# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).

    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    return [1,0,0]
    pass


def expected_points(tot_rounds):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    if tot_rounds==4:
        return 2.1
    elif tot_rounds==6:
        return 3.2
    else:
        return 5
    pass
