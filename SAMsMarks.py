def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >=38:
            f = 5 - grades[i] % 5
            if f<3:
                grades[i] = int(grades[i]) + f

    print(grades)

gradingStudents([73, 67, 38, 33])