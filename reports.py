from queries import welcome

def report_menu(students):
    if len(students) == 0:
        welcome()
        print("No students available")
        Q = input("Press enter to continue: ")
        return

    while True:
        print("\n\n\n\n\n")
        print("-{ Student Evaluation System }-".center(70,'='))
        print("")
        print("-{ Class Analysis }-".center(70,'='))
        print("")
        print("     1. Class Summary")
        print("     2. Subject Average")
        print("     3. Highest Scorer")
        print("     4. Previous menu")

        choice = input("Enter a response: ")

        if choice == "1":
            passed = 0
            failed = 0
            total_percentage = 0

            for i in range(len(students)):
                total_percentage += students[i][7]
                if students[i][9] == "PASS":
                    passed += 1
                else:
                    failed += 1
            print("\n\n\n\n\n")
            print(" Class Summary ".center(70,'-'))
            print()
            print("Total students:", len(students))
            print("Passed:", passed)
            print("Failed:", failed)
            print("Average percentage:", total_percentage / len(students))
            Q = input("Press enter to continue: ")

        elif choice == "2":
            print("\n\n\n\n\n")
            for subject in range(3):
                total = 0
                for i in range(len(students)):
                    total += students[i][subject + 2]
                print("Subject", subject + 1, "average:", total / len(students))
            Q = input("Press enter to continue: ")

        elif choice == "3":
            highest = students[0]

            for i in range(1, len(students)):
                if students[i][8] > highest[8]:
                    highest = students[i]

            print("Highest scorer:", highest[1])
            print("CGPA:", highest[8])
            Q = input("Press enter to continue: ")

        elif choice == "4":
            return

        else:
            print("Enter a valid response")
