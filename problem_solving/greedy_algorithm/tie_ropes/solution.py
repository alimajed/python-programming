def solution(k, input):
    count = 0
    tied_rope_length = 0

    for rope in input:
        tied_rope_length += rope
        if tied_rope_length >= k:
            count += 1
            tied_rope_length = 0

    return count


if __name__ == "__main__":
    print(solution(4, [1,2,3,4,1,1,3]))