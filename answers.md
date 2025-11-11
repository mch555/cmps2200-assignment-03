# CMPS 2200 Assignment 3
## Answers

**Name:**__Maeren Hay_______________________


Place all written answers from `assignment-03.md` here for easier grading.

1a.) 
A greedy algorithm for producing as few coins as possible that sum to N is thel largest denomination first approach.
First we identify the largest coin denomination that is less than or equal to the total amount N (will be in form 2^k).
Taking one coin from that denomination and subtracting its value from the remaining amount, we repeat this process of choosing the largest
possible coin that is less than or equal to N until remainder is 0 (exact change). We know this is possible because our available coin is 2^0=1.

1b.)
**Greedy Choice Property**
the greedy choice is optimal because two coins with denominations 2^i can be replaced by one coin of 2^i+1. Therefore, an optimal solution cannot have 
two or more coins of the same denomination. So the optimal solution for any N is unique and equal to its binary representation! The largest coin 2^k <=N is always included in N's binary 
representation( if N>0) so the greedy choice of taking 2^k works.

**Optimal Substructure Property**
This holds because an optimal solution for the amount N must contain optimal solutions for the smaller remaining amount.
Let C be an optimal set of coins for N, and d be the largest coin chosen (d is the greedy choice).
The remaining set of coins (C complement) C'= C/{d} must be an optimal solution for subproblem N'=N-d.
If C' was not optimal for N', then we wouldfind a smaller set, but this contradicts our assumption that C is our optimal set, 
therefore the optimal solution for N is made from the optimal solution to the subproblem(s) N-d.

1c.)
Work and Span are both W(n)= O(logn) and S(n)=O(logn).

for Work, This is because the algo is the same as finding the binary representation of N. The max num of coins needed is bounded by
the num of bits in N (which is [log2N]+1) and each step takes constant time

for Span, This is because the selection of each coin depends on the remaining amount from the step before, creating a sequential dependency chain, matching the span to work of O(logn).


2a.)
Suppose we have coin denominations D={1, 6, 10} and we want to make change for N=12
The greedy algorithm would choose the largest coin, 10. The remaining amount is 2, which requires two coins of val 1. 

greedy result-> 3 coins (10+1+1)
optimal result->2 coins (6+6)
Therefore the greedy approach is not the optimal choice.
