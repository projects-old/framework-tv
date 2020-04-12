teams = []
x = ""
while x != "XXX":
      x = ""
      print("Enter a team or XXX to quit")
      x = raw_input()
      print(x + " added.")
      if x  != "XXX": 
               teams.append(x)
print("Here are the teams you entered:")
for team in teams: 
       print team
