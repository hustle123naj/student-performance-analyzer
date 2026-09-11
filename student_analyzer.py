
import csv

students = []


# ==========================================
# 1. ADD STUDENTS
# ==========================================

def add_students():
    number = int(input("How many students details: "))

    for i in range(number):
        print("\n---- Enter student details ----")

        name = input("Enter your name: ")
        mark1 = float(input("Enter mark for English: "))
        mark2 = float(input("Enter mark for Maths: "))
        mark3 = float(input("Enter mark for Hindi: "))

        # Calculate total and average
        total = mark1 + mark2 + mark3
        average = total / 3

        # Calculate grade
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "fail"

        # Calculate pass/fail status
        if average >= 50:
            status = "PASS"
        else:
            status = "FAIL"

        # Give feedback
        if average >= 80:
            feedback = "excellent"
        elif average >= 70:
            feedback = "good"
        elif average >= 50:
            feedback = "work harder"
        else:
            feedback = "needs improvement"

        # Create student dictionary
        student = {
            "name": name,
            "total": total,
            "average": average,
            "grade": grade,
            "status": status,
            "feedback": feedback
        }

        # Add student to the list
        students.append(student)

    print("\nStudent details added successfully!")


# ==========================================
# 2. SHOW ALL STUDENTS
# ==========================================

def show_students():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    print("\n--------- STUDENT PERFORMANCE REPORT ---------")

    for student in students:
        print("\nName:", student["name"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("Status:", student["status"])
        print("Feedback:", student["feedback"])


# ==========================================
# 3. SHOW TOP PERFORMER
# ==========================================

def show_top_performer():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    top_student = students[0]

    for student in students:
        if student["average"] > top_student["average"]:
            top_student = student

    print("\n🏆 TOP PERFORMER 🏆")
    print("Name:", top_student["name"])
    print("Average:", round(top_student["average"], 2))
    print("Grade:", top_student["grade"])


# ==========================================
# 4. STUDENTS NEEDING IMPROVEMENT
# ==========================================

def show_students_needing_improvement():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    print("\n⚠️ STUDENTS WHO NEED IMPROVEMENT")

    found = False

    for student in students:
        if student["average"] < 50:
            print("\nName:", student["name"])
            print("Average:", round(student["average"], 2))
            print("Feedback: Needs improvement!")
            found = True

    if found == False:
        print("Great! No students need improvement.")


# ==========================================
# 5. CLASS STATISTICS
# ==========================================

def show_class_statistics():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    print("\n📊 CLASS STATISTICS")

    # Total number of students
    total_students = len(students)

    # Calculate class average
    total_average = 0

    for student in students:
        total_average = total_average + student["average"]

    class_average = total_average / total_students

    # Find highest and lowest average
    highest_average = students[0]["average"]
    lowest_average = students[0]["average"]

    for student in students:

        if student["average"] > highest_average:
            highest_average = student["average"]

        if student["average"] < lowest_average:
            lowest_average = student["average"]

    # Count pass and fail students
    passed_students = 0
    failed_students = 0

    for student in students:

        if student["status"] == "PASS":
            passed_students = passed_students + 1
        else:
            failed_students = failed_students + 1

    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Highest Average:", round(highest_average, 2))
    print("Lowest Average:", round(lowest_average, 2))
    print("Passed Students:", passed_students)
    print("Failed Students:", failed_students)


# ==========================================
# 6. SAVE DATA TO CSV
# ==========================================

def save_to_csv():

    if len(students) == 0:
        print("\nNo student data available to save.")
        return

    with open("student_performance.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Column headings
        writer.writerow([
            "Name",
            "Total",
            "Average",
            "Grade",
            "Status",
            "Feedback"
        ])

        # Write each student's data
        for student in students:
            writer.writerow([
                student["name"],
                student["total"],
                student["average"],
                student["grade"],
                student["status"],
                student["feedback"]
            ])

    print("\nStudent data saved successfully!")


# ==========================================
# 7. READ DATA FROM CSV
# ==========================================

def read_from_csv():

    try:
        print("\n📂 SAVED STUDENT DATA")

        with open("student_performance.csv", "r") as file:

            reader = csv.DictReader(file)

            for student in reader:
                print("\nName:", student["Name"])
                print("Total:", student["Total"])
                print("Average:", student["Average"])
                print("Grade:", student["Grade"])
                print("Status:", student["Status"])
                print("Feedback:", student["Feedback"])

    except FileNotFoundError:
        print("\nCSV file not found.")
        print("Please save student data first.")


# ==========================================
# 8. MAIN MENU
# ==========================================

choice = ""

while choice != "8":

    print("\n======================================")
    print("     STUDENT PERFORMANCE ANALYSER")
    print("======================================")

    print("1. Add Students")
    print("2. Show Students")
    print("3. Top Performer")
    print("4. Students Needing Improvement")
    print("5. Class Statistics")
    print("6. Save to CSV")
    print("7. Read CSV")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_students()

    elif choice == "2":
        show_students()

    elif choice == "3":
        show_top_performer()

    elif choice == "4":
        show_students_needing_improvement()

    elif choice == "5":
        show_class_statistics()

    elif choice == "6":
        save_to_csv()

    elif choice == "7":
        read_from_csv()

    elif choice == "8":
        print("\nThank you for using Student Performance Analyser! 👋")

    else:
        print("\nInvalid choice. Please try again.")

