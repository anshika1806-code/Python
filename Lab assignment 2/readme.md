
def print_welcome():
    print("Welcome to the Gradebook Analyzer!")
    print("This program analyzes student marks for four subjects and provides statistics.")

def get_student_data():
    num_students = int(input("Enter the number of students: "))
    marks = {}
    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        subject_marks = []
        for j in range(4):
            mark = float(input(f"Enter marks for subject {j+1} for {name}: "))
            subject_marks.append(mark)
        average = sum(subject_marks) / 4
        marks[name] = average
    return marks

def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0
    values = sorted(marks_dict.values())
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[n // 2 - 1] + values[n // 2]) / 2

def find_max_score(marks_dict):
    if not marks_dict:
        return 0
    return max(marks_dict.values())

def find_min_score(marks_dict):
    if not marks_dict:
        return 0
    return min(marks_dict.values())

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades_dict):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        distribution[grade] += 1
    return distribution

def pass_fail_lists(marks_dict):
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students

def print_results_table(marks_dict, grades_dict):
    print("\nResults Table:")
    print("Name".ljust(15) + "Average Marks".ljust(15) + "Grade")
    print("-" * 45)
    for name in marks_dict:
        print(f"{name.ljust(15)}{str(round(marks_dict[name], 2)).ljust(15)}{grades_dict[name]}")

def main():
    print_welcome()
    while True:
        marks = get_student_data()
        grades = assign_grades(marks)
        
        # Statistical Analysis
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)
        
        print(f"\nClass Average: {round(avg, 2)}")
        print(f"Median Score: {round(med, 2)}")
        print(f"Max Score: {round(max_score, 2)}")
        print(f"Min Score: {round(min_score, 2)}")
        
        # Grade Distribution
        dist = grade_distribution(grades)
        print("\nGrade Distribution:")
        for grade, count in dist.items():
            print(f"{grade}: {count} students")
        
        # Pass/Fail
        passed, failed = pass_fail_lists(marks)
        print(f"\nPassed Students ({len(passed)}): {passed}")
        print(f"Failed Students ({len(failed)}): {failed}")
        
        # Results Table
        print_results_table(marks, grades)
        
        # Loop option
        choice = input("\nDo you want to re-run the analysis? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
