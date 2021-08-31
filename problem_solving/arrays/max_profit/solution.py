def solution(input):
    global_max_sum = 0
    local_max_sum = 0
    for i in range(1, len(input)):
        delta = input[i] - input[i-1]
        local_max_sum = max(delta, local_max_sum + delta)
        global_max_sum = max(local_max_sum, global_max_sum)

    return global_max_sum

if __name__ == "__main__":
    print(solution([23171,21011,21123,21366,21013,21367]))