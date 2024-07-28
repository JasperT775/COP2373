import csv
import statistics

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

def load_grades_to_numpy_array(filename='grades.csv'):
    # Load the data from the CSV file into a numpy array
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=None, encoding=None)
    return data

def calculate_statistics(data):
    # Extract exam scores
    exam_scores = data[:, 2:].astype(float)
    
    # Calculate and print statistics for each exam
    for i in range(exam_scores.shape[1]):
        print(f"Statistics for Exam {i+1}:")
        print(f"Mean: {np.mean(exam_scores[:, i])}")
        print(f"Median: {np.median(exam_scores[:, i])}")
        print(f"Standard Deviation: {np.std(exam_scores[:, i])}")
        print(f"Minimum: {np.min(exam_scores[:, i])}")
        print(f"Maximum: {np.max(exam_scores[:, i])}")
        print()

    # Calculate and print overall statistics for all exams combined
    all_scores = exam_scores.flatten()
    print("Overall statistics for all exams combined:")
    print(f"Mean: {np.mean(all_scores)}")
    print(f"Median: {np.median(all_scores)}")
    print(f"Standard Deviation: {np.std(all_scores)}")
    print(f"Minimum: {np.min(all_scores)}")
    print(f"Maximum: {np.max(all_scores)}")
    print()

def pass_fail_statistics(data):
    # Extract exam scores
    exam_scores = data[:, 2:].astype(float)
    
    # Determine number of students who passed and failed each exam
    for i in range(exam_scores.shape[1]):
        passed = np.sum(exam_scores[:, i] >= 60)
        failed = np.sum(exam_scores[:, i] < 60)
        print(f"Exam {i+1}: {passed} students passed, {failed} students failed")
    
    # Calculate overall pass percentage across all exams
    total_students = exam_scores.shape[0] * exam_scores.shape[1]
    total_passed = np.sum(exam_scores >= 60)
    pass_percentage = (total_passed / total_students) * 100
    print(f"Overall pass percentage across all exams: {pass_percentage:.2f}%")

def main():
    # Prompt the instructor for how many students to enter
    num_students = int(input("Enter the number of students to enter: "))
    write_grades_to_csv(num_students)
    
    # Read and display data from grades.csv
    read_grades_from_csv()
    
    # Load data into numpy array
    data = load_grades_to_numpy_array()
    
    # Print the first few rows of the dataset
    print("First few rows of the dataset:")
    print(data[:5])
    print()
    
    # Calculate and print statistics
    calculate_statistics(data)
    
    # Calculate and print pass/fail statistics
    pass_fail_statistics(data)

if __name__ == "__main__":
    main()

