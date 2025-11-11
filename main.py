import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def med_top_down(S, T, MED={}):
    ## look up the memory
    if (S, T) in MED:
        return MED[(S, T)]
    ## base cases
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    ## recursive cases
    if S[0] == T[0]:  # If first characters are the same, move to the next
        MED[(S, T)] = med_top_down(S[1:], T[1:], MED)
    else:
        insert = med_top_down(S, T[1:], MED) + 1  # Insert a character
        delete = med_top_down(S[1:], T, MED) + 1  # Delete a character
        MED[(S, T)] = min(insert, delete)
    
    return MED[(S, T)]
    
def fast_MED(S, T):
    n=len(S)
    m=len(T)
    #initialize the DP table
    #DP[i][j] stores the MED between S[:i] and T[:j]
    DP = [[0]* (m+1) for _ in range(n+1)]
    #base case:initialize the first row and column
    for i in range(n+1):
        DP[i][0]=i
    for j in range(m+1):
        DP[0][j]=j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S[i-1]==T[j-1]:
                DP[i][j]=DP[i-1][j-1]
            else:
                DP[i][j]=1 + min(DP[i][j-1], DP[i-1][j])
    return DP[n][m]
           

def fast_align_MED(S, T):
    # TODO - keep track of alignment
    pass

