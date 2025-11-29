Student Data Handling System
    Overview
The Student Data Handling System is a Python-based Command Line Interface (CLI) designed to help school authorities manage academic records. It provides a modular and efficient way to store, retrieve, and analyze student marks across different courses.
The system uses a flat-file database approach (stu.txt) to persist data, allowing users to add new records and perform detailed searches based on student roll numbers or course names.
    Repository Structure
The project is organized into modular scripts:
── main.py          # The entry point (User Interface & Menu Logic)
── addnew.py        # Module for inputting and validating new data
── find.py          # Module for search algorithms and data retrieval
── stu.txt          # Database file (stores student records)
── README.md        # Documentation
    Features
Add Records: Securely input student details (Roll No, Name, Course, Marks).
Search by Course: View all students enrolled in a specific subject (e.g., "Physics").
Student History: View a specific student's performance across all subjects using their Roll Number.
Specific Query: Lookup a specific student's marks in a specific course.
Persistent Storage: Data is saved automatically to stu.txt.
     Prerequisites
Python 3.x installed on your system.
     


Installation
         Clone the repository:
         Bash
         git clone https://github.com/ravirai0207-ctrl/Student_data_handling.git
Navigate to the project directory:
Bash
cd Student_data_handling
Run the Application:
Bash
python main.py
Note: If stu.txt does not exist in the folder, the program may require you to create an empty text file named stu.txt before adding data.
Usage Guide
Follow the on-screen menu prompts:
Select Option 1 to add new student marks.
Select Option 2 to search and display data:
Sub-option 1: Search by Course Name.
Sub-option 2: Search by Roll Number (All courses).
Sub-option 3: Search by Roll Number + Course Name.
Example Workflow
Plaintext
Welcome to School's Portal
What do You Want?
1. Add student's marks
2. Display it?
Answer in 1 or 2: 2
	
1. Want all students data for course
2. A student data in all courses
: 1
Enter course name for which you want data of: Mathematics





Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/NewFeature).
Commit your changes.
Push to the branch.
Open a Pull Request.
License
This project is created by Raviprakash Rai. Created: October 2025

