def solution(input):
    last_end_segment = -1
    chosen_count = 0

    for i in range(len(input)):
        start, end = input[i]
        if start > last_end_segment:
            last_end_segment = end
            chosen_count += 1

    return chosen_count


if __name__ == "__main__":
    print(solution([(1,5),(3,6),(7,8),(9,9),(1,10)]))
    print(solution([(1,2),(3,4),(5,6),(7,8),(9,10)]))