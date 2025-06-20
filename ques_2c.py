import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]
        self.opp_play_styles = [1,1]
        self.points = 1
        self.wins = 1
    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        """
        last = self.results[-1]
        if last == 0:
            return 1
        elif last == 0.5:
            return 0
        else:
            na = sum(self.results)
            nb = len(self.results) - na
            if nb / (na + nb) > 6 / 11:
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
        self.points+=result
        if result==1:
            self.wins+=1
        return
       

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles =[1,1]
        self.results = [0,1]
        self.opp_play_styles = [1,1]
        self.points = 1
        self.wins=1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
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
        if result==1:
            self.wins+=1

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    win, draw, loss = payoff_matrix[alice_move][bob_move]
    r = np.random.uniform(0, 1)
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
        payoff_matrix[0][0][2] = x/(x + y + 1)

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.
    Returns
        Float: estimated value of E[tau]
    """
    ans=0
    no_of_rounds=10**5//T
    for i in range(no_of_rounds):
        payoff_matrix = [[[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]],
                [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 2 / 10]],
                          [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]
        round=2
        alice = Alice()
        bob = Bob()
        while alice.wins<T:
            simulate_round(alice,bob, payoff_matrix)
            round+=1
        ans+=round
    return ans/no_of_rounds
print(estimate_tau(100))
        
        
    