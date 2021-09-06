def find_gcd(a,b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a%b)


def solution(n, m):
    return n // find_gcd(n,m)


if __name__ == "__main__":
    print(solution(10,4))
    print(solution(9,6))
    print(solution(10,11))