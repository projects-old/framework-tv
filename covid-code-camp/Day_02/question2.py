import sys

grade = int(sys.argv[1])

if(grade >= 90):
         letterGrade = "A"
elif(grade >= 80):
         letterGrade = "B"
elif(grade >= 70):
         letterGrade = "C"
elif(grade >= 60):
         letterGrade = "D"
elif(grade >= 50): 
         letterGrade = "F"
else: 

         letterGrade = "F"

print(letterGrade)

