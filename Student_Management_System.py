"""
Student Management System
Language: Python
Description: A menu-driven application to add, view, search, update,
and delete student records. Records are saved permanently in a JSON file.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved records. Starting with an empty list.")
    return []


def save_students(students):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError as error:
        print(f"Could not save records: {error}")


def find_student(students, name):
    for student in students:
        if student["name"].casefold() == name.casefold():
            return student
    return None


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if find_student(students, name):
        print("A student with that name already exists.")
        return

    age_text = input("Enter student age: ").strip()
    if not age_text.isdigit() or int(age_text) <= 0:
        print("Please enter a valid positive age.")
        return

    course = input("Enter student course: ").strip()
    if not course:
        print("Course cannot be empty.")
        return

    students.append({"name": name, "age": int(age_text), "course": course})
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")
    for number, student in enumerate(students, start=1):
        print(f"{number}. Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")


def search_student(students):
    name = input("Enter student name to search: ").strip()
    student = find_student(students, name)
    if student:
        print("\nStudent found!")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
    else:
        print("Student not found.")


def update_student(students):
    name = input("Enter student name to update: ").strip()
    student = find_student(students, name)
    if not student:
        print("Student not found.")
        return

    new_age = input("Enter new age (press Enter to keep current age): ").strip()
    if new_age:
        if not new_age.isdigit() or int(new_age) <= 0:
            print("Please enter a valid positive age.")
            return
        student["age"] = int(new_age)

    new_course = input("Enter new course (press Enter to keep current course): ").strip()
    if new_course:
        student["course"] = new_course

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    name = input("Enter student name to delete: ").strip()
    student = find_student(students, name)
    if not student:
        print("Student not found.")
        return

    confirmation = input(f"Delete {student['name']}? (y/n): ").strip().lower()
    if confirmation == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
