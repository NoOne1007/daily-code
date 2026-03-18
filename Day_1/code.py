print("Day-1: Getting Started")

def f():
    try:
        x = 10
        return x
    finally:
        x = 20
        return x

print(f())