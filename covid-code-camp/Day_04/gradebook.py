#import prettytable and sys
#import sys
from prettytable import PrettyTable

# enter student names and grades to create a book of grades. exit by entering XXX

student = ""
gradebook = {}

print("Enter XXX to stop entering students.")

while student != "XXX":
    student = raw_input("Name: ")
    if student != "XXX":
        grade = int(raw_input("Grade: "))
        print("\n")
        gradebook.update({student: grade})
   #else:
        #sys.exit("Exiting without changes.")

# running statistics
lowStud = ""
lowGrade = 9999 # set impossible high number as nobody can get this
highStud = ""
highGrade = 0
average = 0
amountStudents = 0
print("\n")
print("Here are all the students you entered and their grades:")
table = PrettyTable(['Student', 'Grade'])
for stud, grade in gradebook.items():
    table.add_row([stud, grade])
    average = average + grade
    amountStudents = amountStudents + 1
    # find low and high
    if grade < lowGrade: 
        lowStud = stud
        lowGrade = grade
    if grade > highGrade:
        highStud = stud
        highGrade = grade
average = average / amountStudents
print table
print("\n")
print("Average grade earned: " + str(average))
print("\n")
print("Highest grade: " + str(highGrade) + " |" + " Student: " + highStud)
print("\n")
print("Lowest grade: " + str(lowGrade) + " |" + " Student: " + lowStud)
