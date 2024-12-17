class Student:
    grade = 3
    name = "Momo"

    def introduction(self):
        print("Hi! I am a student")

    def details(self):
        print("My name is: ", self.name)
        print("My grade is: ", self.grade)

ob = Student()
ob.introduction()
ob.details()
        