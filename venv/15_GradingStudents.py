def gradingStudents(grades):
    newgrades = []
    for grade in grades:

        if grade < 38:
            newgrades.append(grade)
        else:
            new = grade // 5
            new += 1
            newGrade = new * 5
            diff = newGrade - grade
            if diff < 3:
                newgrades.append(newGrade)
            else:
                newgrades.append(grade)

    return newgrades
