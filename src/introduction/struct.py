students = []

typeName = "Bob"
typeDorm = "Site"

for i in range(3):
    name = typeName
    dorm = typeDorm

    student = {"name": name, "dorm0": dorm}
    students.append(student)

for student in students:
    print(f"{student['name']} is in this {student['dorm0']}")