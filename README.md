# Student Data Handling System

##  Overview
The **Student Data Handling System** is a Python-based Command Line Interface (CLI) designed to help school authorities manage academic records efficiently. It provides a modular approach to store, retrieve, and analyze student marks across different courses using a flat-file database (`stu.txt`).

## Repository Structure
The project is organized into modular scripts:

* `main.py`: The entry point (User Interface & Menu Logic).
* `addnew.py`: Module for inputting and validating new data.
* `find.py`: Module for search algorithms and data retrieval.
* `stu.txt`: Database file (stores student records).
* `README.md`: Project Documentation.

## Features
* **Add Records:** Securely input student details (Roll No, Name, Course, Marks).
* **Search by Course:** View all students enrolled in a specific subject (e.g., "Physics").
* **Student History:** View a specific student's performance across all subjects using their Roll Number.
* **Specific Query:** Lookup a specific student's marks in a specific course.
* **Persistent Storage:** Data is saved automatically to `stu.txt`.

## Prerequisites
* Python 3.x installed on your system.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ravirai0207-ctrl/Student_data_handling.git](https://github.com/ravirai0207-ctrl/Student_data_handling.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Student_data_handling
    ```

3.  **Run the Application:**
    ```bash
    python main.py
    ```

##  Usage Guide
Follow the on-screen menu prompts:

1.  Select **Option 1** to add new student marks.
2.  Select **Option 2** to search and display data:
    * *Sub-option 1:* Search by Course Name.
    * *Sub-option 2:* Search by Roll Number (All courses).
    * *Sub-option 3:* Search by Roll Number + Course Name.

	
### Contributing
1. Fork the repository.
2. Create a feature branch (git checkout -b feature/NewFeature).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

### License & Author
 This project is created by Raviprakash Rai.
### Example Workflow
```text
Welcome to School's Portal
What do You Want?
1. Add student's marks
2. Display it?
Answer in 1 or 2: 2
    
1. Want all students data for course
2. A student data in all courses
: 1
Enter course name for which you want data of: Mathematics





