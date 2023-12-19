class Student:
    
    studentsList = []

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    
    def getName(self):
        return self.name
    
    def getRating(self):
        return self.rating



Student.studentsList.append(Student("Noah", 1875))
Student.studentsList.append(Student("Boah", 69))
Student.studentsList.append(Student("Shoah", 420))

for student in Student.studentsList:
    print("Name: " + student.getName())
    print("Rating: " + str(student.getRating()) + '\n')