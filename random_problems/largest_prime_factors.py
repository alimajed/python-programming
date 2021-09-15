def main():
    number = 600851475143
    e_number = number
    largest_prime_factor = 0

    counter = 2
    while counter * counter <= e_number:
        print(counter, e_number)
        if e_number % counter == 0:
            e_number = e_number // counter
            largest_prime_factor = counter
        else:
            counter += 1

    if e_number > largest_prime_factor:
        largest_prime_factor = e_number

    print(largest_prime_factor)

if __name__ == "__main__":
    main()