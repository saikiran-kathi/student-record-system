# Student Record System using File Handling

while True:
    print("\nStudent Record System")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as file:
            file.write(f"{name}, {roll}, {marks}\n")

        print("Student record added successfully.")

    elif choice == "2":
        print("\nStudent Records:")
        try:
            with open("students.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        print("Exiting Student Record System.")
        break

    else:
        print("Invalid choice. Please try again.")
