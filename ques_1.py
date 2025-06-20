"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""

M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))


# Problem 1a
def helperfn(n1,n2):
    l = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]
    l[1][1] = 1
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if i == 1 and j == 1:
                continue
            l[i][j] = mod_add(mod_multiply(l[i - 1][j] , mod_divide(j , (i + j - 1))) , mod_multiply(l[i][j - 1],mod_divide(i , (i + j - 1))))

    return l
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    return helperfn(alice_wins,bob_wins)[bob_wins][alice_wins]
# Problem 1b (Expectation)
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    expectation=0
    l=helperfn(t,t)
    for i in range(1,t):
        expectation=mod_add(expectation,mod_multiply(2*i-t,l[i][t-i]))
    return expectation
# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    variance=0
    l=helperfn(t,t)
    for i in range(1,t):
        variance = mod_add(variance, mod_multiply((2 * i - t) ** 2, l[i][t-i]))
    return variance
