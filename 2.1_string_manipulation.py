"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: write a sentence
# 2. Process: shorted a sentance in four ways
# 3. Out: Four different printed lines.
# 4. My four transformations, and when each is useful: learned uppercase,lowercase,titlecase and reversed


# Your code below
sentence = input("Sentence:")

# 1. Uppercase
print(sentence.upper())

# 2. Lowercase
print(sentence.lower())

# 3. Title Case (first letter of each word capitalized)
print(sentence.title())

# 4. Reversed
print("Reversed:", sentence[::-1])


