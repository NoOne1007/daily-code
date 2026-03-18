# Day 1

## What I Did

* Setup GitHub repo
* Practiced basic Python

## Key Learning

* Initialized Git repo and first commit

## Time Taken

~10 mins

## Notes

Starting simple. Focus is consistency.

## Interesting Learning

### finally overrides return

```
def f():
    try:
        return 10
    finally:
        return 20
```
Output: 20

Insight:
- finally always executes before function exit
- return inside finally overrides previous return
- should generally avoid return in finally
