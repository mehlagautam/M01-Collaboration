# Author: Gautam Mehla
# File Name: student_qualification.py
# Description: This app accepts student names and GPAs and determines if they qualify for the Dean's List or the Honor Roll.

def check_qualification(gpa):
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.25:
        return "Honor Roll"
    else:
        return None

def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        qualification = check_qualification(gpa)

        if qualification:
            print(f"{first_name} {last_name} has made the {qualification}.")
        else:
            print(f"{first_name} {last_name} does not qualify for any honors.")

if __name__ == "__main__":
    main()
