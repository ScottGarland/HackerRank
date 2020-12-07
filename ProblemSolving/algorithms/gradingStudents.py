def gradingStudents(grades):

    rounded = []

    for g in grades:
        if (g < 38) or ((g % 5) < 3) :
            rounded.append(g)
        else:
            rounded.append(g + (5 - (g % 5)))

    return rounded
