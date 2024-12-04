#The authors' names are Victoria, Maggie, Anna, and Serentiy
#The __str__() FUnction

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+ str(self.age) + ")"

p1 = Person("John", 36)

print(p1)
