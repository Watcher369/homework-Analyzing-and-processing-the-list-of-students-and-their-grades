

def calculate_average(grades):
    return sum(grades) / len(grades)


def calculate_student_average(student):
    grades = student["grades"]
    return calculate_average(grades)


def is_students_empty(students):
    if not students:
        print("Список студентов пуст.")
        return True

    return False


def show_students_info(students):
    if is_students_empty(students):
        return

    for student in students:
        average_score = calculate_student_average(student)
        print(f"\nСтудент: {student['name']}")
        print(f"Средний балл: {average_score:.2f}")
        print(f"Статус: {get_status_of_student(average_score)}")


def get_status_of_student(average_score):
    status = "Успешен" if average_score >= 75 else "Отстающий"
    return status


def calculate_group_average(students):
    total_average = 0

    for student in students:
        total_average += calculate_student_average(student)

    return total_average / len(students)


def show_group_average(students):
    if is_students_empty(students):
        return

    group_average = calculate_group_average(students)
    print(f"Общий средний балл: {group_average:.2f}")


def get_student_name():
    while True:
        name = input("Введите имя студента: ").strip()

        if name:
            return name

        print("Ошибка: имя студента не должно быть пустым.")


def get_grades():
    while True:
        grades_text = input("Введите оценки через пробел: ")

        try:
            grades = []

            for grade in grades_text.split():
                grades.append(int(grade))

            for grade in grades:
                if grade < 0 or grade > 100:
                    print("Ошибка: оценки должны быть от 0 до 100.")
                    break
            else:
                if len(grades) < 3:
                    print("Ошибка: введите минимум 3 оценки через пробел. Например: 80 90 75")
                    continue

                return grades

        except ValueError:
            print("Ошибка: оценки должны быть числами. Например: 80 90 75")


def add_new_student(students):
    name = get_student_name()
    grades = get_grades()

    new_student = {
        "name": name,
        "grades": grades
    }

    students.append(new_student)

    print(f"Студент {new_student['name']} добавлен.")
    show_group_average(students)


def find_lowest_student(students):
    lowest_student = students[0]
    lowest_average = calculate_student_average(lowest_student)

    for student in students:
        average_score = calculate_student_average(student)

        if average_score < lowest_average:
            lowest_average = average_score
            lowest_student = student

    return lowest_student


def show_lowest_student(students):
    if is_students_empty(students):
        return

    lowest_student = find_lowest_student(students)
    lowest_average = calculate_student_average(lowest_student)

    print(f"Студент с самым низким средним баллом: {lowest_student['name']}")
    print(f"Средний балл: {lowest_average:.2f}")


def delete_student_with_lowest_grades(students):
    if is_students_empty(students):
        return

    lowest_student = find_lowest_student(students)
    students.remove(lowest_student)
    print(f"Студент {lowest_student['name']} удален.")
    show_group_average(students)


def main(students):
    menu = {
        "1": ["Показать информацию о студентах", show_students_info],
        "2": ["Показать общий средний балл", show_group_average],
        "3": ["Добавить нового студента", add_new_student],
        "4": ["Показать студента с самым низким средним баллом", show_lowest_student],
        "5": ["Удалить студента с самым низким средним баллом", delete_student_with_lowest_grades],
        "0": ["Завершить программу", None],
    }

    while True:
        print("\nМеню:")

        for key, value in menu.items():
            print(f"{key}. {value[0]}")

        choice = input("\nВыберите действие: ")

        if choice == "0":
            print("Программа завершена.")
            break

        if choice in menu:
            menu[choice][1](students)
        else:
            print("Ошибка: выберите пункт из меню.")


if __name__ == "__main__":

    students = [
        {"name": "Гарри", "grades": [80, 90, 78]},
        {"name": "Гермиона", "grades": [95, 99, 97]},
        {"name": "Рон", "grades": [60, 70, 64]},
        {"name": "Драко", "grades": [60, 75, 70]},
    ]

    main(students)