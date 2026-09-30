

def welcome():
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

def rank_students(students):
    ranked = students[:]

    for i in range(len(ranked)):
        for j in range(i + 1, len(ranked)):
            if ranked[j][8] > ranked[i][8]:
                temp = ranked[i]
                ranked[i] = ranked[j]
                ranked[j] = temp

    return ranked


def query_menu(students):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return

    while True:
        print("\n\n\n\n\n")
        print("-{ Student Related Queries }-".center(70,'='))
        print()
        print("     1. Ranking")
        print("     2. Students with 10 CGPA")
        print("     3. Students with full marks")
        print("     4. Pass/Fail list")
        print("     5. Previous menu")

        choice = input("Enter a response: ")

        if choice == "1":
            ranked = rank_students(students)
            print("\n\n\n\n\n")
            for i in range(len(ranked)):
                print(i + 1, ranked[i][1], "| CGPA:", ranked[i][8])
            Q = input("Press enter to continue: ")
            

        elif choice == "2":
            found = 0
            print("\n\n\n\n\n")
            for i in range(len(students)):
                if students[i][8] == 10:
                    print(students[i][1], "|", students[i][0])
                    found = 1

            if found == 0:
                print("No student secured 10 CGPA")
            Q = input("Press enter to continue: ")

        elif choice == "3":
            found = 0
            print("\n\n\n\n\n")
            for i in range(len(students)):
                if students[i][5] == students[i][6]:
                    print(students[i][1], "|", students[i][0])
                    found = 1
            if found == 0:
                print("No student secured full marks")
            Q = input("Press enter to continue: ")

        elif choice == "4":
            print("\n\n\n\n\n")
            print(" Pass/Fail List ".center(50,'-'))
            for i in range(len(students)):
                print(students[i][1], "|", students[i][9])
            Q = input("Press enter to continue: ")

        elif choice == "5":
            return

        else:
            print("Enter a valid response")
