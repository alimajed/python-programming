def calculate_factorial(num):
    # fact = 1
    # while num > 0:
    #     fact *= num
    #     num -= 1
    # return fact
    if num <= 1:
        return 1
    return num * calculate_factorial(num-1)


if __name__ == "__main__":
    print(calculate_factorial(5))