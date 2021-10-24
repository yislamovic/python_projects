txt = open("employees.txt", "a+")
txt.write("\nappended text")
txt.close()
t = open("employees.txt", "r")
for employee in t.readlines():
  print employee
