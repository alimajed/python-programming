def solution(max, input):
    total_slices = 0
    in_current_slices = [False] * (max + 1)
    head = 0
    tail = 0

    for tail in range(0, len(input)):
        # NOTE the tail will advance only when we exit this loop
        while head < len(input) and (not in_current_slices[input[head]]):
            in_current_slices[input[head]] = True
            total_slices += (head - tail) + 1
            head += 1
        in_current_slices[input[tail]] = False
        
    return total_slices


if __name__ == "__main__":
    print(solution(9, [2,4,1,7,4,9,7,3,5,5,8,7,1]))
    print(solution(6, [3,4,5,5,2]))