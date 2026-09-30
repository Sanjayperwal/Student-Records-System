from student import add_student, view_student, update_student, delete_student, show_students
from queries import query_menu
from reports import report_menu

students = []


while True:
    print("\n\n\n\n\n")
    print(" Enter the Maximum marks for evalaution ".center(80,'-'))
    print("")
    print(" CGPA, total, and the result will highly depends on this value")
    print(" and it is required ")
    print("")
    max_marks = input("Enter:  ")

    if max_marks.isdigit() and int(max_marks) > 0:
        max_marks = int(max_marks)
        break

    print("Enter valid maximum marks")


def welcome1():
    print("\n\n\n\n\n")
    print("-{ Student Evaluation System }-".center(70,'='))
    print("")
    print("     1. Add Student")
    print("     2. View Student")
    print("     3. Update Student")
    print("     4. Delete Student")
    print("     5. View All Students")
    print("     6. Student Queries")
    print("     7. Class Analysis")
    print("     8. Exit")


while True:
    welcome1()
    choice = input("Enter a response: ")

    if choice == "1":
        add_student(students, max_marks)
    elif choice == "2":
        view_student(students)
    elif choice == "3":
        update_student(students, max_marks)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        show_students(students)
    elif choice == "6":
        query_menu(students)
    elif choice == "7":
        report_menu(students)
    elif choice == "8":
        print("Program ended")
        break
    else:
        print("Enter a valid response")
