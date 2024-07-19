import math
import random



def random_number():
    num1 = int(input("Enter first number in the range "))
    num2 = int(input("Enter the second number in the range "))
    start = min(num1, num2)
    end = max(num1, num2)
    numbers=list(range(start, end))
    guessin_number = (random.choice(numbers))

    z = end - start
    i = 0
    while i <= math.log2(z):
        x = int(input(f"Now guess the number between {start} and {end} "))
        if x == guessin_number:
            print("Great you guessed the right number")
            break
        elif x < guessin_number:
            print("Try again, you chose a smaller number.")
        elif x > guessin_number:
            print("Try again, you chose a bigger number.")
        i = i + 1
    if i > math.log2(z):
        print("You have exhausted the Minimum number of guesses")


random_number()