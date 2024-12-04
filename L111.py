#The authors' names are Victoria, Maggie, Anna, and Serentiy
#A: The __init__() function

#I think it'll print the name of the person name and years old 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#My guess was right, however I was expencting to not be right, I tought it was going to print something like __class__() and then the perosn with name and age.

p2 = Person("Victoria", 19)

print(p2.name)
print(p2.age)

