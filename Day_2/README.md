# Day 2

## What I Did

* Explored how `__name__` works in Python
* Created two files to understand behavior during direct execution vs import:

  * `file_1.py`
  * `file_2.py`

---

## Code Structure

### file_1.py

* Prints its `__name__`
* Contains a check for direct execution

### file_2.py

* Imports `file_1`
* Prints its own `__name__`
* Contains a check for direct execution

---

## Output (when running file_2.py)
```
file_1 name: file_1
file_2 name: **main**
file_2 is being run directly
```
---

## Key Learning

* When a file is run directly → `__name__ = "__main__"`
* When a file is imported → `__name__ = "<file_name>"`
* Python executes all top-level code in a file when it is imported
* `if __name__ == "__main__"` ensures code runs only when the file is executed directly

---

## Why This Matters

* Helps separate reusable code from execution logic
* Prevents unintended execution when importing modules
* Common pattern in real-world Python projects

---

## Time Taken

~30 mins

---

## Notes

* Important concept for writing modular and reusable Python code
* Will be useful when working on larger projects
