students = [90, 45, 64, 29, 17, 9]
result = []

for student in students:
    if student >= 71 :
        result.append("A")
    elif student >= 41 :
        result.append("B")
    elif student >= 11 :
        result.append("C")
    elif student <= 10:
        result.append("D")

print(result)





