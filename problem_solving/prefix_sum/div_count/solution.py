from math import cail, floor 


def solution(a,b,k):
    return floor(b/k) - ceil(a/k) + 1


if __name__ == "__main__":
    print(solution(4,17,2))