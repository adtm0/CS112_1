#Prompt user for student information
name = input("Student name: ")
idno = input("ID #: ")
course = input("Course: ")
section = input("Section: ")
q1 = eval(input("1st Quarter Grade: "))
q2 = eval(input("2nd Quarter Grade: "))
q3 = eval(input("3rd Quarter Grade: "))
q4 = eval(input("4th Quarter Grade: "))

#Compute Average
average = ((q1+q2+q3+q4)/4)

#Display Student information and Average Grade
print(
" Name: ", name,'\n',
"ID No.: ", idno,'\n',
"Course: ", course,'\n',
"Section: ", section,'\n',
"1st Quarter Grade: ", q1,'\n',
"2nd Quarter Grade: ",q2,'\n',
"3rd Quarter Grade: ",q3,'\n',
"4th Quarter Grade: ",q4,'\n',
"Average: ", average)
