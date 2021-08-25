def solution(input, n):
    # NOTE init our counters array
    counters = [0] * n
    start_line = 0
    # NOTE maximum counter value
    current_max = 0

    for i in input:
        # NOTE index start by zero, but in the instruction list starts by 1
        x = i-1
        # NOTE first case to check if max_counter
        if i > n:
            start_line = current_max
        # NOTE check if counter value is behind the starting line
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1
        # NOTE keep our current max updated
        if i <= n and counters[x] > current_max:
            current_max = counters[x]

    # NOTE move counter that are behine the startline to the startline
    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line
    
    return counters
    

if __name__ == "__main__":
    print(solution([3,4,4,6,1,4,4], 5))