# Inheritance in Python
# 1. It is a mechanism in which one class acquires the property of another class.
# 2. The class whose properties are acquired are known as Parent class.
# 3. The class that inherits the previous class are known as Child class.
# 4. The child class can access all the data members and functions of the parent class.
# 5. The child class can also provide its specific implementation to the functions of the parent class.
# 6. The child class can also extend the functionality of the parent class.
# 7. The child class can also override the functions of the parent class.
# 8. The child class can also inherit the properties of multiple parent classes.


class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Isu", 30)
e1.showDetails()

e2 = Programmer("Atul", 21)
e2.showDetails()

e2.showLanguage()
