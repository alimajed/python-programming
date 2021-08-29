def solution(directions, weights):
    stack = []
    survivors = 0
    for i in range(len(directions)):
        weight = weights[i]
        # NOTE swimming to the right
        if directions[i] == 1:
            stack.append(weight)
        else:
            weight_down = stack.pop() if stack else -1
            # NOTE keep comparing the fishes in the stack with the current item
            # # if the fish in the stack is smaller, we throw it and we pop again
            while weight_down != -1 and weight_down < weight:
                weight_down = stack.pop() if stack else -1
            # NOTE the stack is empty
            if weight_down == -1:
                survivors += 1
            # NOTE return the fish to the stack 
            else:
                stack.append(weight_down)

    return survivors + len(stack)


if __name__ == "__main__":
    print(solution([0,1,1,0,0], [4,8,2,6,7]))
    print(solution([0,1,0,0,0], [4,3,2,1,5]))
