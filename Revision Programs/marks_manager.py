name_of_students = {}

def add_students():
    student_name = input("Enter student name: ")
    try:
        student_marks = int(input("Enter student marks: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    name_of_students[student_name] = student_marks
    print(f"{student_name} has been added with marks {student_marks}")

def calc_average():
    if not name_of_students:
        print("No students has been added yet.")
        return
    average = sum(name_of_students.values()) / len(name_of_students)
    print(f"Average marks: {average:.2f}")

def highest_lowest():
    if not name_of_students:
        print("No students has been added yet.")
        return
    highest = max(name_of_students, key=name_of_students.get)
    lowest = min(name_of_students, key=name_of_students.get)
    print(f"Highest marks: {highest} -> {name_of_students[highest]}")
    print(f"Lowest marks: {lowest} -> {name_of_students[lowest]}")

def assign_grades():
    if not name_of_students:
        print("No students has been added yet.")
        return
    print("Assign grades: ")
    for student, marks in name_of_students.items():
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"
        print(f"{student}: {marks} -> {grade}")

def view_students():
    if not name_of_students:
        print("No students has been added yet.")
        return
    print("\nAll Students and Marks")
    for student, marks in name_of_students.items():
        print(f"{student}: {marks}")

def menu_list():
    while True:
        print("\n--- Student Marks Manager ---")
        print("1. Add Student")
        print("2. Calculate Average")
        print("3. Highest & Lowest Marks")
        print("4. Assign Grades")
        print("5. View All Students")
        print("6. Exit")

        user_choice = input("Choose an option from 1 to 6: ")

        if user_choice == "1":
            add_students()
        elif user_choice == "2":
            calc_average()
        elif user_choice == "3":
            highest_lowest()
        elif user_choice == "4":
            assign_grades()
        elif user_choice == "5":
            view_students()
        elif user_choice == "6":
            print("Thank you for using this program.")
            break
        else:
            print("Choose a valid option!")

menu_list()
