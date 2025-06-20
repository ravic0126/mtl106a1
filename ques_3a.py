import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        """
        prob_defence=0.4984848485
        prob_balance=0.45
        prob_attack=1/3*(len(self.results)-self.points)/len(self.results)+(1/3)*7/10+1/3*5/11
        if prob_attack>=prob_defence:
            return 0
        else:
            return 2
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.opp_play_styles.append(opp_style)
        self.results.append(result)
        self.points += result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1]
        self.results = [0,1]
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.opp_play_styles.append(opp_style)
        self.results.append(result)
        self.points += result

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    win, draw, loss = payoff_matrix[alice_move][bob_move]
    r = np.random.uniform(0, win + draw + loss)
    is_win = False
    is_draw = False
    is_loss = False
    if r < win:
        is_win = True
    elif r < win + draw:
        is_draw = True
    else:
        is_loss = True
    x = alice.points
    y = bob.points
    if is_win == True:
        alice.observe_result(alice_move, bob_move, 1)
        bob.observe_result(bob_move, alice_move, 0)
        payoff_matrix[0][0][0] = y / (x + y + 1)
        payoff_matrix[0][0][2] = (x + 1) / (x + y + 1)
    elif is_draw == True:
        alice.observe_result(alice_move, bob_move, 0.5)
        bob.observe_result(bob_move, alice_move, 0.5)
        payoff_matrix[0][0][0] = (y + 0.5) / (x + y + 1)
        payoff_matrix[0][0][2] = (x + 0.5) / (x + y + 1)
    else:
        alice.observe_result(alice_move, bob_move, 0)
        bob.observe_result(bob_move, alice_move, 1)
        payoff_matrix[0][0][0] = (y + 1) / (x + y + 1)
        payoff_matrix[0][0][2] = (x) / (x + y + 1)

    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    pay_off_matrix = [[[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]],
                      [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 2 / 10]],
                      [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]
    alice = Alice()
    bob = Bob()
    for i in range(2, num_rounds):
        simulate_round(alice, bob, pay_off_matrix)
    print(pay_off_matrix)
    print(alice.points, bob.points)
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)