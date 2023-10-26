STUDENTS = 5
SEPARATOR = '*' * 75

list_students = []
list_grade_first_exam = []
list_grade_second_exam = []
list_average = []

for i in range(STUDENTS):

    student = input("\nIngrese el nombre del alumno > ").strip().capitalize()
    while not student or not student.isalpha():
        student = input("\n¡Error! Debe ingresar valido, vuelva a intentarlo > ").strip().capitalize()

    while True:
        try:
            grade_first_exam = int(input("\nIngrese la nota del primer parcial > ").strip())
            while grade_first_exam < 0 or grade_first_exam > 10:
                grade_first_exam = int(input("\n¡Error! Debe ingresar caracteres numéricos, vuelva a intentarlo > ").strip())
            break

        except ValueError:
            print("\n¡Error! La nota debe ser un valor numérico entre 0 y 10.")
            continue

    while True:
        try:
            grade_second_exam = int(input("\nIngrese la nota del segundo parcial > ").strip())
            while grade_second_exam < 0 or grade_second_exam > 10:
                grade_second_exam = int(input("\n¡Error! Debe ingresar caracteres numéricos, vuelva a intentarlo > ").strip())
            break

        except ValueError:
            print("\n¡Error! La nota debe ser un valor numérico entre 0 y 10.")
            continue

    

    list_students.append(student)
    list_grade_first_exam.append(grade_first_exam)
    list_grade_second_exam.append(grade_second_exam)

for i in range(len(list_students)):
    average = (list_grade_first_exam[i] + list_grade_second_exam[i]) / 2

    list_average.append(average)

    print()
    print(SEPARATOR)

    print("\nAlumno: {0} | Primer nota: {1} | Segunda nota: {2} | Promedio: {3:.2f}".format(list_students[i], 
                                                                                        list_grade_first_exam[i],
                                                                                        list_grade_second_exam[i],
                                                                                        list_average[i]))
    
print(SEPARATOR)
