class Student():
  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa
  
  def honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

  def _probation(self):
    if self.gpa >= 2.0:
      return False
    else:
      return True

