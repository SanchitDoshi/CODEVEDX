#  Utility Usage Prediction Tool

> AI/ML Internship Project 1 – CODEVEDX

##  Project Description

The **Utility Usage Prediction Tool** is a Machine Learning-based console application developed using Python. It helps users manage electricity usage records and predict future electricity consumption using historical data.

The application provides CRUD (Create, Read, Update, Delete) operations for electricity usage records stored in a CSV file. A Linear Regression model is trained using the available data to estimate electricity consumption for future days.

This project demonstrates the practical implementation of Python programming, data handling, and basic Machine Learning techniques.

---

#  Objectives

- Develop a menu-driven console application.
- Learn CSV file handling using Pandas.
- Implement CRUD operations.
- Build a Machine Learning prediction model.
- Understand Linear Regression.
- Improve Python programming skills.

---

#  Features

✔ Add New Electricity Usage Record

✔ Update Existing Record

✔ Delete Record

✔ View Complete Dataset

✔ Predict Future Electricity Usage

✔ CSV File Handling

✔ Exception Handling

✔ User-Friendly Console Interface

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| Scikit-learn | Machine Learning |
| Linear Regression | Prediction Algorithm |
| CSV | Data Storage |
| VS Code | Code Editor |

---

#  Machine Learning Algorithm

## Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict continuous values. It learns the relationship between historical electricity usage and the day number to estimate future consumption.

---

#  Dataset

**File Name**

Project1.csv

**Columns**

| Column            | Description                  |
|-------------------|------------------------------|
| Day               | Day Number                   |
| Electricity_Usage | Electricity Consumed (Units) |

---

#  Project Structure

Project_Utility Usage Prediction Tool (ML – Console)/

│── Screenshots/

│── Project1.py

│── Project1.csv

│── README.md

│── Project1_PPT.pptx

│── Project1_Report.pdf

---

#  Installation

Clone the repository

```bash
git clone https://github.com/SanchitDoshi/CODEVEDX.git
```

Install required libraries

```bash
pip install pandas scikit-learn
```

Run the project

```bash
python Project1.py
```

---

#  Sample Output

```text
UTILITY USAGE PREDICTION TOOL

1. Add Data
2. Update Data
3. Delete Data
4. View Data
5. Predict Usage
6. Exit

Enter Choice: 5

Enter Future Day: 35

Predicted Electricity Usage: 218.68 Units
```

---

#  Future Improvements

- Add Graphical User Interface (GUI)
- Store data in MySQL
- Generate usage reports
- Display graphs using Matplotlib
- Deploy using Flask

---

#  Learning Outcomes

Through this project I learned:

- Python Programming
- Pandas
- CSV Handling
- Exception Handling
- Machine Learning Basics
- Linear Regression
- Git & GitHub

---

#  Author

**Sanchit Doshi**

Artificial Intelligence & Machine Learning Intern

CODEVEDX

---

#  License

This project is created for educational purposes as part of the CODEVEDX AI/ML Internship.