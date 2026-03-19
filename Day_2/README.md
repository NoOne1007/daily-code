# Day 2

## What I Did

* Explored how `__name__` works in Python
* Created two files to understand behavior during direct execution vs import:

  * `file_1.py`
  * `file_2.py`

* Created three files to understand behavior during direct execution vs import:
  * `file_a.py`
  * `file_b.py`
  * `file_c.py`

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
* Python executes code top-to-bottom. When it encounters an import statement, it pauses the current module, executes the imported module once, then resumes execution
