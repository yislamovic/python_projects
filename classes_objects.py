class Student:
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation
  
  def honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

student1 = Student('Yahya', 'comp', 2.85, True)
student2 = Student('Job', 'marketing', 3.95, False)

print student1.honor_roll()
print student2.honor_roll()