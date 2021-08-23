# Cyclic Rotation Problem

## Definition
- Given an input list of numbers and rotation argument k, every number in the list shifts to the right k times.
- In cyclic rotation, the last number in the list become the first number.
- Here is an example:
    ```
    input = [3,5,7,2,8] 
    k = 2

    # Solution
    input
    >>> [2,8,3,5,7]
    ```
- Our target is to find a solution with linear time complexity O(n) and linear space complexity O(n).


## Hints
- Thinking about solving the problem using reminder trick
- What is a reminder? and what is the reminder trick
- Giving this example:
    - 501 / 2 = 250 REM 1
    - 501 / 10 = 50 REM 1
    - 509 / 10 = 50 REM 9
    - 510 / 10 = 51 REM 0

    The reminder cannot be greater than the divisor.
- We use the modulo oprator (%) to get the reminder.


## Solution
- let's say that s is the size of the input list
- Iterate over each number, the magic formula to get the new position after the shifting is **(index+k)%5**


## Code
    def solution(input, k):
        size = len(input)
        new_list = [None]*size
        for i in range(0, size):
            new_index = (i+k)%size
            new_list[new_index] = input[i]
        
        return new_list
