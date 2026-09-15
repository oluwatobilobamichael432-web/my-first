def grade():

    students = [
            ["Samuel", 80, 75, 90],
            ["David", 55, 60, 50],
            ["Mary", 35, 40, 30],
            ["John", 65, 70, 68]
        ]

    for student in students:
        average = float(student[1] + student[2] + student[3]) / 3
        name = student[0]

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 45:
            grade = "D"
        elif average >= 40:
            grade = "E"
        else:
            grade = "F"
        print(f"{name} - Average: {average} - Grade: {grade}")


grade()