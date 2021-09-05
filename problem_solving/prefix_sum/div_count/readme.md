# Div Count Problem


## Definition
- We are given a sequence of numbers increment by one each time, we need to find the number of multiples that exists in the sequence of a particular factor.
- For example a list [6,7,8,9,10,11] and k=2 as factor, will result len([6,8,10]) => 3
- We are getting 2 numbers, the start and the end of the sequence.
- Our target is to find a solution with constant time complexity O(1) and constant space complexity O(1).


## Hints
- Let's say we have start=4, end=17, and the factor is 3.
- The returned result is 4, and the values are [6,9,12,15]
- The first multiple is 6 (3*2) and the last multiple is 15 (3*5)
- By simple math expression we can find the solution.


## Solution
- We can conclude that the result is the last multiple value minus the first one plus one 4 = 5 - 2 + 1
- The difficulty here is to find these two boundaries, the first and the last multiple.
- It is simply dividing the start and the end of the sequence by the factor:
    - For the start pick the closest integer that comes after.
    - For the end pick the closest integer that comes before.


## Code