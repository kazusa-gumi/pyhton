'''
class Animal:
    def speak(self):
        print("Anumal speaks")

my_animal = Animal()
my_animal.speak()
'''

class student: 
    schol_name="Holmesglen"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = student("peter", 504)
print(s1.name, s1.roll_no, student.schol_name)

s2 = student("Poll", 555)
print(s2.name, s2.roll_no, student.schol_name)

