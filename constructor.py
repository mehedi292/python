class Student:
    roll = ""
    cgpa = ""

    def __init__(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, cgpa: {self.cgpa}") 


rahim = Student(101, 3.50)
rahim.display()


jahid = Student(102,3.60)
jahid.display()


jannat = Student(103,3.80)
jannat.display()
