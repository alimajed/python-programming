def main():
    p = 0
    n = 1
    sum = 0
    total = 0
    count = 0
    print(p)
    print(n)
    while sum < 4000000:
        sum = n + p
        p = n
        n = sum
        if sum % 2 == 0:
            total += sum
        count += 1
    print(total)

if __name__ == "__main__":
    main()