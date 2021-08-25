def solution(input, x):
    # NOTE the values of the input list starts by one
    # # so we initialize the lookup array starting by 1 and ending by x+1
    river_positions = [False] * (x+1)
    for time in range(len(input)):
        pos = input[time]
        if not river_positions[pos]:
            river_positions[pos] = True
            x -= 1
            if x == 0: return time

    return -1

    
if __name__ == "__main__":
    print(solution([1,3,1,4,2,3,5,4], 5))