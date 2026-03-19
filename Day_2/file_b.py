print("Executing file_b")

import file_a

def func_b():
    print("Inside func_b")
    file_a.func_a()

if __name__ == "__main__":
    print("file_b is run directly")
    func_b()