# Class creation 
class Myclass:
    x=5
# object creation 
obj1= Myclass()
print(obj1.x)

## __init__ function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Umair",25)
print(p1.name)
print(p1.age)
print(p1)

### string representation of an object 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p2 = Person("Umair",25)
print(p2)


## object Methods
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def myfun(self):
        print(self.name)
        print(self.age)
    
obj1 = Person("Umair",25)
print("calling object Method")
obj1.myfun()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.age = 25
p1.myfunc()
print(p1.age)

# delete object perameter 
del p1.age

# print(p1.age)  # it will show the Error 


# class inheritence 

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)

x = Person("Muhammad","Umair")
x.printname()

#creation of clild Class
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduation = year
    def welcome(self):
        print("welcome",self.firstname,self.lastname, " to the class of graguation", self.graduation)




x = Student("MEri","Malik",2025)
x.welcome()


## python iterators

print("\n python iterators")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
    
obj = MyNumbers()
myiter = iter(obj)
# loop to print 10 iters we can print one by one 

for i in range(10):
    print(next(myiter))


# if we want to stop  after some iteratin 
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

obj = MyNumbers()
myiter = iter(obj)
# loop to print 10 iters we can print one by one 

for i in myiter:
    print(i)


## Polymorphism
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Driver!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Sahil!")
    
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

#we cAN BE USE Polymarphism in inheritence of the class
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move")


class Car(Vehicle):
    # def move(self):
    #     print("Drive")
    pass

class Boat(Vehicle):
    def move(self):
        print("Sahil!")


class Plane(Vehicle):
    def move(self):
        print("fly")


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

