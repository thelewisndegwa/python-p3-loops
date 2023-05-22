#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print('Happy New Year!')
        i -= 1
    pass

def square_integers(int_list):
    squared_numbers = ([num ** 2 for num in int_list])
    print(squared_numbers)
    return squared_numbers
    pass

def fizzbuzz():
    for num in range (1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass

# happy_new_year()
square_integers([-1,-2,-3,-10,-20])
# fizzbuzz()