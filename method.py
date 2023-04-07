class Student:
    roll = ""
    cgpa = ""

    def set_Value(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, cgpa: {self.cgpa}") 


rahim = Student()
rahim.set_Value(101, 3.50)
rahim.display()





jahid = Student()
jahid.roll = 102
jahid.cgpa = 3.70


jannat = Student()
jannat.roll = 103
jannat.cgpa = 3.80
