import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

FILE_NAME =r"Project2.csv"



def load_data():

    sample_data = {
        "Student_ID": list(range(1, 21)),
        "Attendance": [
            90, 85, 70, 95, 80,
            88, 76, 92, 65, 98,
            82, 87, 73, 91, 78,
            84, 69, 94, 89, 96
        ],
        "Study_Hours": [
            5, 4, 2, 6, 3,
            5, 4, 6, 2, 7,
            4, 5, 3, 6, 4,
            5, 2, 6, 5, 7
        ],
        "Assignment_Score": [
            85, 80, 65, 90, 75,
            84, 72, 89, 60, 95,
            78, 83, 68, 90, 74,
            81, 63, 91, 86, 94
        ],
        "Internal_Marks": [
            80, 75, 60, 88, 72,
            82, 70, 90, 58, 94,
            76, 81, 66, 89, 73,
            80, 61, 90, 84, 93
        ],
        "Final_Marks": [
            84, 78, 62, 91, 74,
            85, 71, 92, 59, 96,
            77, 83, 67, 90, 74,
            81, 62, 91, 85, 95
        ]
    }

    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(sample_data)
        df.to_csv(FILE_NAME, index=False)
        print("Sample dataset created.")
        return df

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        df = pd.DataFrame(sample_data)
        df.to_csv(FILE_NAME, index=False)
        print("File was empty. Sample data added.")

    return df


def display_data():
    df = load_data()
    print(df)


def show_info():
    df = load_data()
    print("\nDataset Information\n")
    print(df.info())
    print("\nMissing Values\n")
    print(df.isnull().sum())


def visualize():
    df = load_data()

    plt.figure(figsize=(6,4))
    plt.scatter(df["Study_Hours"], df["Final_Marks"])
    plt.title("Study Hours vs Final Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Marks")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(6,4))
    plt.bar(df["Student_ID"], df["Final_Marks"])
    plt.title("Student Performance")
    plt.xlabel("Student ID")
    plt.ylabel("Final Marks")
    plt.show()


def train_model():
    df = load_data()

    X = df[["Attendance","Study_Hours","Assignment_Score","Internal_Marks"]]
    y = df["Final_Marks"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train,y_train)

    prediction = model.predict(X_test)

    accuracy = r2_score(y_test,prediction)

    print("\nModel Accuracy:",round(accuracy*100,2),"%")

    return model


def predict():
    model = train_model()

    attendance = float(input("Enter Attendance: "))
    study = float(input("Enter Study Hours: "))
    assignment = float(input("Enter Assignment Score: "))
    internal = float(input("Enter Internal Marks: "))

    data = pd.DataFrame({
        "Attendance":[attendance],
        "Study_Hours":[study],
        "Assignment_Score":[assignment],
        "Internal_Marks":[internal]
    })

    result = model.predict(data)

    print("\nPredicted Final Marks:",round(result[0],2))


while True:

    print("\nSTUDENT PERFORMANCE PREDICTION SYSTEM")
    print("1. View Dataset")
    print("2. Dataset Information")
    print("3. Data Visualization")
    print("4. Train Model")
    print("5. Predict Student Performance")
    print("6. Exit")

    try:

        choice = int(input("Enter Choice: "))

        if choice == 1:
            display_data()

        elif choice == 2:
            show_info()

        elif choice == 3:
            visualize()

        elif choice == 4:
            train_model()

        elif choice == 5:
            predict()

        elif choice == 6:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print("Error:",e)