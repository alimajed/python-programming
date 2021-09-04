def solution(input):
    prefix_sum = [0] * (len(input) + 1)
    # NOTE calculate the prefix ssum
    for i in range(len(input)):
        prefix_sum[i+1] = prefix_sum[i] + input[i]
    
    count = 0
    for i in range(len(input)):
        if input[i] == 0:
            count += (prefix_sum[len(input)] - prefix_sum[i+1])

    return count

if __name__ == "__main__":
    print(solution([0,1,0,1,1]))
