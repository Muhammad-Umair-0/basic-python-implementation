class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name {self.name}")

    



obj = User("Umair",24)
obj.show()

print('Name', getattr(obj, 'name'))
print('age ', getattr(obj, 'age'))


# add dynamically instance variable to class 
obj.marks = 75
print(obj.marks)

# dell any object dynamically 
del obj.marks
# print(obj.marks)

delattr(obj, 'name')
# obj.show()

# access instance from another class

class Vehicle:
    def __init__(self):
        self.engine = '1500cc'
    
class Car(Vehicle):
    def __init__(self, maxSpeed):
        super().__init__()
        self.maxSpeed = maxSpeed

    def Display(self):
        print(f"Engine : {self.engine}  speed : {self.maxSpeed}")

car_obj = Car(240)
car_obj.Display()

# to get list of all instance objects 

print(car_obj.__dict__)


# class variables and instance variables 

class Student:
    # class variables
    school_name = "ABC school"
    # constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # instance Methods
    def show(self):
        print(f"Student {self.name, self.age, self.school_name}")
    # instance method
    def change_age(self,new_age):
        self.age = new_age
    
    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name


# object creation 

obj_stud = Student("mari",25)
print(obj_stud.school_name)
print(obj_stud.age)
obj_stud.show()


s1 = Student('hamza',24)
print("THe ")
# called instant method 

s1.show()
s1.change_age(13)
s1.show()

Student.modify_school_name("hkjshkfjhksdjf")
s1.show()