def find_student(students, reg_no):
    for i in range(len(students)):
        if students[i][0].lower() == reg_no.lower():
            return i
    return -1


def add_record(students, record):
    students.append(record)


def delete_record(students, index):
    students.pop(index)
