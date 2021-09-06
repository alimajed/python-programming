# The Euclidian Algorithm

## Definition
- It is a useful algorithm when we want to find the greatest common divisor (GCD) between two numbers


## Explinations
- Find the GCD between A=39 and B=27
    ```
        A    B   | Find how many times number B fit in A                             A + B
        39,  27 --> 1, reminder 12                                              |     66
        27,  12 --> 2, reminder 3                                               |     39
        12,   3 --> 4, reminder 0                                               |     15
         3,   0 --> our stopping condition when B is zero, A is the solution    |      3
    ```

## Code (Recursive)
    def GCD(A,B):
        if B==0:
            return A
        else:
            return GCD(B, A%B)