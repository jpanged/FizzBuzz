# FizzBuzz Game
# Date: 07-31-2017
# Author: Josiah Pang

# How FizzBuzz Works:
# "FizzBuzz" is a game that counts up to a value one at a time. If the number is
# a multiple of 3, "Fizz" is displayed instead of the number. If the number is
# a multiple of 5, "Buzz" is displayed instead of the number. If the number is
# a multiple of both, "FizzBuzz" is displayed.

# Plays the "FizzBuzz" game to 100
def fizzbuzz():
    for i in range(1, 101):
        word = ''
        if (i % 3) == 0:
            word += 'Fizz'
        if (i % 5) == 0:
            word += 'Buzz'
        if word != '':
            print(word)
        else:
            print(i)

fizzbuzz()
