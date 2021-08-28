# Brackets Problem


## Definition
- We have a string as input, only contains the brackets characters
- Our solution should return if the brackets in the string are properly nested
- Examples of the valid input string
    - **[()()]**
    - **[({})]**
    - **[](){}[][]{}()**
    - ...
- Examples of the not valid input string
    - **][**
    - **[())]**
    - ...


## Hints
- Use Stacks to solve the problem


## Solution
- Whenever we meet and left bracket (open) we push to the stack
- whenever we meet and right bracket, we pop whatever we have in the stack, and we check if it is the equivalent bracket to the current one
- After checking all characters, we check whether the stack is empty (success) or not (fail).


## Code
    def solution(s):
        valid = True
        stack = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif c == "]":
                valid = False if not stack or stack.pop() != "[" else valid
            elif c == ")":
                valid = False if not stack or stack.pop() != "(" else valid
            elif c == "}":
                valid = False if not stack or stack.pop() != "{" else valid
        if valid and not stack:
            return True
        return False
