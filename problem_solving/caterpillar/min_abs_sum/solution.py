def solution(input):
    min_abs_sum = None
    # NOTE sort the input list
    input = sorted(input)
    head = 0
    tail = len(input) - 1

    while head <= tail:
        if not min_abs_sum:
            min_abs_sum = abs(input[head] + input[tail])
        else:
            min_abs_sum = min(min_abs_sum, abs(input[head] + input[tail]))
        # NOTE move head pointer forward
        if input[head] + input[tail] < 0:
            head += 1
        # NOTE move tail pointer backward
        else:
            tail-= 1

    return min_abs_sum


if __name__ == "__main__":
    print(solution([-7,3,-1,5,-11,4,-9,14,17,-2]))
    print(solution([8,3,5,16,11]))
    print(solution([-7,-5,-6,-2,-9]))