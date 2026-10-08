# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-08 07:12, in .

**Me:** how to i read semicolon csv

**Tutor:**

Reading a CSV file with semicolons as delimiters.

```python
import csv

def read_semicolon_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        # TODO: Iterate over the reader to process each row
        for row in reader:
            # TODO: Handle each row here
            pass
```

What is the name of the parameter that specifies the delimiter in `csv.reader`?
