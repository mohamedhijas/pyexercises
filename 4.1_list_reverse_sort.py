"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The list from exercise 4.0 is written in the code: ten numbers (10, 9, 1, 7, 8, 6, 2, 3, 4, 5).
# 2. Process: provide a backup copy of the list, then builds four reordered versions without changing the original. At the end it compares the original with the backup to prove nothing changed.
# 3. Out:the list in four orders, then the original list again and a True/False check that it is identical to the backup.
# 4. My four orders, and which ones modify the original:Ascending with sorted: a new list, the original not modified. Descending with sorted: a new list, original not modified. Reversed: a new list, original not modified. Ascending with .sort on a copy: .sort changes, but I used it a copy, so the original is not modified. If I had called .sort or .reverse directly on the original list, it would have been modified. None of my four orders do that.


# Your code below
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]
backup = list_of_numbers.copy()
print("copy:", list_of_numbers)

print("Original list:", list_of_numbers)

# order 1: ascending (new list)
print("1. Ascending:", sorted(list_of_numbers))

# order 2: descending (new list)
print("2. Descending:", sorted(list_of_numbers, reverse=True))

# order 3: reversed (new list)
print("3. Reversed:", list_of_numbers[::-1])

# order 4: .sort() works in place, so I use it on a copy
copy_of_list = list_of_numbers.copy()
copy_of_list.sort()
print("4. Ascending using .sort() on a copy:", copy_of_list)

# proof that the original is not damaged
print("Original list at the end:", list_of_numbers)
print("Same as the backup?", list_of_numbers == backup)

