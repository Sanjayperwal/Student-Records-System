# Student Records & Evaluation System

## About the Project

The **Student Records & Evaluation System** is a simple command-line Python project developed for the VITyarthi **Build Your Own Project** activity.

The system manages student records and evaluates academic performance. It can add, view, update and delete students, calculate total marks, percentage and CGPA, check PASS/FAIL status, rank students, answer common student queries, and generate basic class reports.

## Student Details

- **Student:** Sanjay Perwal
- **Registration No.:** 26MIM10155
- **Faculty:** Dr. Kannan Shanmugam Sir
- **Project Type:** Individual – Build Your Own Project
- **Date:** September 2026
- **Slots:** B11 + B12 + B13 + C14 + E11 + E12

## Features

- Add student
- View student
- Update student
- Delete student
- View all students
- Calculate total marks
- Calculate percentage
- Calculate CGPA
- Check PASS/FAIL status
- Student ranking
- Find students with 10 CGPA
- Find students with full marks
- Class summary
- Subject-wise average
- Highest scorer
- Input validation
- Basic automated testing

## Technologies Used

- Python 3
- Git
- GitHub

## Project Structure

```text
Student-Records-System/
├── main.py
├── student.py
├── queries.py
├── reports.py
├── storage.py
├── test_student_evaluation.py
├── README.md
└── statement.md
```

### File Description

- `main.py` – Main program and menu control.
- `student.py` – Student CRUD operations, marks validation and result calculation.
- `queries.py` – Ranking and student-related queries.
- `reports.py` – Class summary, subject averages and highest-scorer analysis.
- `storage.py` – Basic student record search, add and delete operations.
- `test_student_evaluation.py` – Tests for result calculation, storage and ranking.
- `statement.md` – Project problem statement, scope and target users.

## How to Run

Open the project folder in a terminal and run:

```bash
python main.py
```

If required:

```bash
python3 main.py
```

## Result Calculation

```text
Total = Subject 1 + Subject 2 + Subject 3

Percentage = (Total / Maximum Total) × 100

CGPA = Percentage / 10
```

A student is marked **PASS** when each subject has at least 40% of the configured maximum marks.

## Student Record

Each student record contains:

```text
Registration No.
Student Name
Subject 1 Marks
Subject 2 Marks
Subject 3 Marks
Total Marks
Maximum Total
Percentage
CGPA
PASS / FAIL Status
```

## Queries and Reports

### Student Queries

1. Ranking
2. Students with 10 CGPA
3. Students with full marks
4. PASS/FAIL list

### Class Analysis

1. Class summary
2. Subject average
3. Highest scorer

## Testing

The project includes `test_student_evaluation.py`.

Run the tests with:

```bash
python test_student_evaluation.py
```

The tests cover:

- Result calculation
- PASS/FAIL calculation
- Adding and finding a student
- Deleting a student
- Student ranking

## Project Purpose

This project demonstrates practical Python concepts including:

- Variables and data types
- Input and output
- Operators and calculations
- Conditional statements
- Loops
- Lists
- Functions
- Searching
- Sorting/ranking
- Input validation
- Modular programming
- Basic testing

## Future Enhancements

- Add permanent JSON or file-based storage.
- Support more subjects.
- Make pass marks configurable.
- Add a graphical user interface.
- Export results to CSV/PDF.
- Add login and role-based access.

## GitHub Repository

https://github.com/Sanjayperwal/Student-Records-System.git

## Author

**Sanjay Perwal**  
Registration No.: **26MIM10155**

**VITyarthi – Build Your Own Project**
