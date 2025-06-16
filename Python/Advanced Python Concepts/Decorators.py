def hello():
    print("Hello World!")

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx()
    
@greet
def add():
    print(a + b)

hello()