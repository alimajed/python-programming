def main():
    multiples_set = set()
    for i in range(1, 10):
        if i%3==0 or i%5==0:
            multiples_set.add(i)
    print(multiples_set)
    print(sum(multiples_set))


if __name__ == "__main__":
    main()