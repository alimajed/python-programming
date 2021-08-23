def solution(input):
    max_number = len(input) + 1
    expected_sum = (max_number * (max_number + 1)) / 2
    actual_sum = 0
    for i in input:
        actual_sum += i

    return expected_sum - actual_sum

if __name__ == "__main__":
    print(solution([2,3,1,5]))
    print(solution([1,2,3,4,5,6,7,8,9]))
    print(solution([]))