grades = {    "Mark": 78, 
              "Jennifer": 83, 
              "Stacey": 90, 
              "Jason": 61,
              "Seth": 90,
              "Thomas": 70,
              "Evander": 100
}

print(grades["Mark"])
print(grades["Seth"])
#print(grades["Horatio"])
grades["Jason"] = 88
print(grades)
grades.update({"Sammie": 67})
grades.update({"Maria": 80})
del grades["Mark"]
#grades.clear()
#del grades

for student, grade in grades.items():
	print(student + " earned a grade of " + str(grade))

print("\n")
for grade in grades.values():
	print(str(grade))

print("\n")
for student in grades:
	print(student)
