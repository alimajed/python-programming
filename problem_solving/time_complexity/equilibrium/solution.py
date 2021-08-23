def solution(input):
    sum_left = input[0]
    sum_right = sum(input) - input[0]
    diff = abs(sum_left - sum_right)
    p=1
    for i in range(1, len(input)):
        sum_left += input[i]
        sum_right -= input[i]
        current_diff = abs(sum_left - sum_right)
        if current_diff < diff:
            diff = current_diff
            # NOTE i should in included in the right part
            p = i+1
    return p


if __name__ == "__main__":
    print(solution([3,1,2,4,3]))