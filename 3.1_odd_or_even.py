"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Enter the a number
# 2. Process:the program checks number first. If it is valid, a loop goes through every number from 1 to N, and the % operator (remainder after dividing by 2) decides whether each number is odd or even.
# 3. Out: display A number is odd or even
# 4. What happens on 0, on a negative number, on a very large number:0: the program prints a message and stops, because there are no numbers between 1 and 0 to check. On a negative number: same message, because the range 1 to N is empty.  On a very large number (above 1000): the program refuses and asks for a smaller number, because printing thousands of lines is not useful.


# Your code below
MAX_N = 1000

n = int(input("Enter a number N: "))

if n <= 0:
    print("Please enter a number greater than 0.")
elif n > MAX_N:
    print("That number is too large. Please enter", MAX_N, "or less.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
