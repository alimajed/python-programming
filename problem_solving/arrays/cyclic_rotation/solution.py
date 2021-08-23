def solution(input, k):
    size = len(input)
    new_list = [None]*size
    for i in range(0, size):
        new_index = (i+k)%size
        new_list[new_index] = input[i]
    
    return new_list

if __name__ == "__main__":
    print(solution([1,2,3,4,5,6], 4))