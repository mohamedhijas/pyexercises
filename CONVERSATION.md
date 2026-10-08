# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-08 07:12, in .

**Me:** how to i read semicolon csv

**Tutor:**

Reading a CSV file with semicolons as delimiters.

```python
import cs

def read_semicolon_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        # TODO: Iterate over the reader to process each row
        for row in reader:
            # TODO: Handle each row here
            pass
```

What is the name of the parameter that specifies the delimiter in `csv.reader`?

---
## 2026-10-08 07:57, in .

**Me:** how to i read semicolon csv

**Tutor:**

Reading a CSV with semicolons uses the csv module and the delimiter argument.

```python
import csv

def read_semicolon_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # TODO: iterate over reader and print each row
```

What is the name of the argument that tells csv.reader to use a semicolon as the delimiter?

---
## 2026-10-08 08:10, in .

**Me:** how to print name and age

**Tutor:**

Printing two values means you need to combine them into one string.
Use the `print()` function and separate the values with a comma.

```python
def print_name_and_age(name, age):
    # TODO: combine name and age into one print statement
    pass
```

What is the separator between the two values when you use `print(name, age)`?
