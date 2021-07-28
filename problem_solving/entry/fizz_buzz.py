"""
Given a positive integer, N, print all the integers from 1 to N.
For multiples of 3 print "Fizz" instead of the number and for multiples of 5
print "Buzz". For numbers which are multiples of 3 and 5, print "FizzBuzz".
https://blog.codinghorror.com/why-cant-programmers-program/
"""
if __name__ == "__main__":
    n = 15

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)