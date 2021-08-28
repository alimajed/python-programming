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


if __name__ == "__main__":
    print(solution("[({})]"))
    print(solution("[({"))
