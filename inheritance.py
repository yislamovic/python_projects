from classes_objects import Student
class Mentor(Student):
  def __init__(self, name, major, gpa):
      super().__init__(name, major, gpa)

  def is_elligable_mentor(self):
    if self._probation:
      return False
    else: 
      return True



student1 = Student('Yahya', 'CompSci', 3.5)
student2 = Student('Job', 'Marketing', 1.6)
mentor1 = Mentor('Yahya', 'CompSci', 3.5)

print(student1.honor_roll())
print(student2.honor_roll())
print(mentor1.is_elligable_mentor())
