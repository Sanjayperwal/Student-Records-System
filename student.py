from storage import find_student, add_record, delete_record
from queries import welcome

def get_marks(max_marks):
    marks = []

    for i in range(3):
        while True:
            mark = input("Enter marks of Subject " + str(i + 1) + ": ")

            if mark.isdigit():
                mark = int(mark)
                if mark >= 0 and mark <= max_marks:
                    marks.append(mark)
                    break

            print("Enter valid marks")

    return marks


def calculate_result(marks, max_marks):
    total = marks[0] + marks[1] + marks[2]
    maximum = max_marks * 3
    percentage = total * 100 / maximum
    cgpa = percentage / 10

    if marks[0] >= max_marks * 0.4 and marks[1] >= max_marks * 0.4 and marks[2] >= max_marks * 0.4:
        status = "PASS"
    else:
        status = "FAIL"

    return total, maximum, percentage, cgpa, status


def add_student(students, max_marks):
    name = input("Enter Student name: ")
    reg_no = input("Enter Registration no.: ")

    if name == "" or reg_no == "":
        welcome()
        print("Name and Registration number cannot be empty")
        Q = input("Press enter to continue: ")
        return

    if find_student(students, reg_no) != -1:
        welcome()
        print("Registration number already exists")
        Q = input("Press enter to continue: ")
        return

    marks = get_marks(max_marks)
    total, maximum, percentage, cgpa, status = calculate_result(marks, max_marks)

    record = [reg_no, name, marks[0], marks[1], marks[2], total, maximum, percentage, cgpa, status]
    add_record(students, record)
    print("Student added successfully".center(70,'\''))
    #welcome()
    Q = input("Press enter to continue: ")


def view_student(students):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return

    reg_no = input("Enter Registration no.: ")
    index = find_student(students, reg_no)

    if index == -1:
        welcome()
        print("Student not found")
        Q = input("Press enter to continue: ")
        return

    student = students[index]
    print("\n\n\n\n\n")
    print("Name:        ", student[1])
    print("Reg. No.:    ", student[0])
    print("Subject 1:   ", student[2])
    print("Subject 2:   ", student[3])
    print("Subject 3:   ", student[4])
    print("Total:       ", student[5], "/", student[6])
    print("Percentage:  ", student[7])
    print("CGPA:        ", student[8])
    print("Status:      ", student[9])
    Q = input("Press enter to continue: ")


def update_student(students, max_marks):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return

    reg_no = input("Enter Reg. No.: ")
    index = find_student(students, reg_no)

    if index == -1:
        welcome()
        print("Student not found")
        Q = input("Press enter to continue: ")
        return

    name = input("Enter new name: ")
    if name == "":
        name = students[index][1]

    marks = get_marks(max_marks)
    total, maximum, percentage, cgpa, status = calculate_result(marks, max_marks)

    students[index] = [reg_no, name, marks[0], marks[1], marks[2], total, maximum, percentage, cgpa, status]
    print("Student updated successfully".center(70,'\''))
    Q = input("Press enter to continue: ")
    


def delete_student(students):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return

    reg_no = input("Enter Registration no.: ")
    index = find_student(students, reg_no)

    if index == -1:
        welcome()
        print("Student not found")
        Q = input("Press enter to continue: ")
        return

    confirm = input("Delete this student? Y/N: ").lower()

    if confirm == "y":
        delete_record(students, index)
        print("Student deleted successfully".center(70,'\''))
        Q = input("Press enter to continue: ")


def show_students(students):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return
    print("\n\n\n\n\n")
    for i in range(len(students)):
        print(i+1, students[i][1], "|", students[i][0], "| CGPA:", students[i][8], "|", students[i][9])
    Q = input("Press enter to continue: ")
