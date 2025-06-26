# Creating Classes
print("Excamples of how to Create Classes\n")

class Foo:
    def show(self):
        print("Hi!")

def add_attribute(self):
    self.z = 9

Test = type("Test", (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test()
t.add_attribute()
print(t.z)
t.show()

# Creating MetaClasses
print("\nExamples of how to make MetaClasses\n")

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        
        print(a)
        return type(class_name, bases, a)
        
class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
print(d.HELLO())