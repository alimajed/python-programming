# Perm Missing Element Problem

## Definition
- Given an unordered list of numbers starting from 1, having a missing element.
- In the problem, we have an input list of n elements, where its elements are in range 1 and n+1.
- In this example, we have this list and 6 is the missing element
    ```
    input = [3,1,5,3], n = 4 ==> missing element is 6
    ```
- Our target is to find a solution with linear time complexity O(n) and linear space complexity O(n)


## Hints
- Using brute force, by iterating over each item
    ```
    for i in range(1, n+1):
        if i in input:
            return i
        else:
            continue
    ```
    the runtime complexity of this solution is quadratic O(n^2)
- Using a hash table (dict in python), or lookup table
    ```
    lookup = [None] * (n+1)
    for i in range(1, n+1):
        lookup[i] = 1
    for i in lookup:
        if not lookup[i]:
            return i
    ```
    the runtime complexity of this solution is linear O(n), but we are adding extra structure to the memory having space complexity O(n).


## Solution
- The solution is the sum of everything, the sum of numbers in range 1 and n+1 is the expected sum if the list does have the missing element.
- So the expected sum minus the sum of the number in the input.
- This solution has a linear runtime complexity O(n) and constant space complexity O(1).
- We can slightly improve the method to calculate the expected sum instead of using sum(1, n+1) using a mathematic formula (x * (x+1)) / 2 where x = n + 1 (sum to n formula).


## Code
    def solution(input):
        max_number = len(input) + 1
        expected_sum = (max_number * (max_number + 1)) / 2
        actual_sum = 0
        for i in input:
            actual_sum += i

        return expected_sum - actual_sum
