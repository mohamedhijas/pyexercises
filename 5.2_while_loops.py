"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The list (number) is by written in the code
# 2. Process: the program takes the first and second items by index,and squares. finds each item's position with index. Then a for loop repeats the same steps for every item in the list.
# 3. Out:the item, its position in the list, and its square. The first two items are printed one by one, then all twelve are printed by the loop.
# 4. My stop condition, my attempt limit, my summary: Practice list for using twelve numbers. Stop condition: the for loop ends by itself after the last item. Attempt limit: none, because a for loop cannot run forever. Summary: no summary is printed.


# Your code below
list = [5, 6, 7, 8, 1, 2, 3, 4, 9, 10, 11, 12]

i = list[0]
print(i)
print(list.index(i))
print(i**2)

item2 = list[1]
print(item2)
print(list.index(item2))
print(item2**2)


# using for loop to iterate through the list and print the item, its position, and its square
print("The list is:", list)
for i in list:
    print("The item is:", i, "and its position in the list is:", 
          list.index(i), "and the square of the item is:", i**2)
