# Demo Program 1

# file = open("file.txt", "r")
# try:
#     file.write("Hello World!")
# finally:
#     file.close()
    
# with open("file.txt", "r") as file:
#     file.write("Hello World!")
    

# Demo Program 2

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file
    
    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        if type == Exception:
            return True


with File("file.txt", "w") as f:
    print("Middle")
    f.write("Hello World!")
    

# Demo Program 3

import contextlib
from contextliv import contextmanager

@contextlib.contextmanager
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yield file
    file.close()
    print("exit")


with file("text.txt", "w") as f:
    print("Middle")
    f.write("HelLo Coders!")    