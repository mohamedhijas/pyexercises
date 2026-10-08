"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Type answer, "yes" or "no", in the second loop. The first loop takes no input.
# 2. Process:the first loop counts i from 0 to 9, adding 1 each time, and stops  when i < 10 becomes false. The second loop asks again and again. It cleans the answer with strip and lower, and stops with break on "yes" or "no"
# 3. Out:the numbers 0 to 9, a "finished" line with the final i 10, then a message for "yes" or "no", or an error message for anything else.
# 4. What I compute for each item, and why it is worth showing: Learned is the loop counter, i + 1 on every pass. printing i on every pass lets me see the loop count up and stop when i reaches 10. It proves the condition works and that the loop cannot run forever.


# Your code below
i = 0
while i < 10:
    print("The value of i is:", i)
    i += 1

print("The loop has finished. The final value of i is:", i)

while True:
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
    if answer == "yes":
        print("You chose to continue.")
        break
    elif answer == "no":
        print("You chose to stop.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")