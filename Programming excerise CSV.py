import csv

def write_grades_to_csv(num_students):
    # Open the grades.csv file in write mode with 'newline='' to ensure no extra newline characters are added
    with open('grades.csv', 'w', newline='') as file:
        # Define the header for the CSV file
        fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row to the CSV file
        writer.writeheader()

        # Loop through each student
        for _ in range(num_students):
            # Get input from the instructor for each student's details
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 score: "))
            exam2 = int(input("Enter Exam 2 score: "))
            exam3 = int(input("Enter Exam 3 score: "))

            # Write the student's data as a row in the CSV file
            writer.writerow({'First Name': first_name, 'Last Name': last_name,
                             'Exam 1': exam1, 'Exam 2': exam2, 'Exam 3': exam3})

    print(f"Successfully wrote {num_students} records to grades.csv")

def read_grades_from_csv():
    # Open the grades.csv file in read mode
    with open('grades.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)

        # Print header
        print(f"{'First Name':<12} {'Last Name':<12} {'Exam 1':<8} {'Exam 2':<8} {'Exam 3':<8}")
        print("-" * 50)

        # Iterate over each row in the CSV file
        for row in reader:
            # Print each student's data formatted in a tabular format
            print(f"{row['First Name']:<12} {row['Last Name']:<12} {row['Exam 1']:<8} {row['Exam 2']:<8} {row['Exam 3']:<8}")

def main():
    # Prompt the instructor for how many students to enter
    num_students = int(input("Enter the number of students to enter: "))
    write_grades_to_csv(num_students)

    # Read and display data from grades.csv
    read_grades_from_csv()

if __name__ == "__main__":
    main()
