print ("Day 003 Activity")

# A) display 10 through 20
print("--- Print 10 through 20")
x = 10
while x <= 20:
    print(x)
    x = x + 1
print("--------")

# B) display 100 through 0 by 5s
print("--- print 100 through 0 by 5s")
x = 100
while x >= 0:
    print(x)
    x = x - 5
print("--------")

# C) display 1 through 100 but all even numbers are X
print("--- print 1 through 100 but even numbers a X")
x = 1
while x <= 100:
    if((x % 2) == 0):
        print("X")
    else:
        print(x)
    x = x + 1
print("--------")

# D) display 5 through 25 on the same line
print("--- print 5 through 25 on the same line")
x = 5
output = ""
while x <= 25:
    output = output + " " + str(x)
    x = x + 1
print(output)
print("--------")
