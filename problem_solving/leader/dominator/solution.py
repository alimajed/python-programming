def solution(input):
    candidate_counter = 0
    candidate = 0
    for i in input:
        if candidate_counter == 0:
            candidate = i
            candidate_counter = 1
        elif candidate == i:
            candidate_counter += 1
        else:
            candidate_counter -= 1
    
    if candidate:
        occurences = input.count(candidate)
        if occurences >= len(input)/2:
            return input.index(candidate)
    return -1


if __name__ == "__main__":
    print(solution([3,0,1,1,4,1,1]))