import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    #edited to use fast_MED
    return fast_MED(S, T)

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
    n = len(S)
    m = len(T)
    #compute the DP table
    DP = [[0]* (m+1) for _ in range(n+1)]
    
    #base case: initialize the first row and column
    for i in range(n+1):
        DP[i][0] = i
    for j in range(m+1):
        DP[0][j] = j
    
    #fill DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S[i-1] == T[j-1]:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = 1 + min(DP[i][j-1], DP[i-1][j])

   
    S_align = []
    T_align = []
    i = n
    j = m

    while i > 0 or j > 0:
        #base case: Already at (0, j) boundary
        if i == 0:
            S_align.append('-')
            T_align.append(T[j-1])
            j -= 1
            continue
        
        #base case: Already at (i, 0) boundary
        if j == 0:
            S_align.append(S[i-1])
            T_align.append('-')
            i -= 1
            continue
        
        #check if characters match
        if S[i-1] == T[j-1]:
            S_align.append(S[i-1])
            T_align.append(T[j-1])
            i -= 1
            j -= 1
        else:
            #characters don't match - check insertion vs deletion
            insert_cost = DP[i][j-1]
            delete_cost = DP[i-1][j]
            
            #prioritize insertion when costs are equal
            if insert_cost <= delete_cost:
                S_align.append('-')
                T_align.append(T[j-1])
                j -= 1
            else:
                S_align.append(S[i-1])
                T_align.append('-')
                i -= 1

    #reverse and join
    return "".join(S_align[::-1]), "".join(T_align[::-1])
