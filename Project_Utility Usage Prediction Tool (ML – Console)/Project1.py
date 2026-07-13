import pandas as pd
from sklearn.linear_model import LinearRegression
import os

FILE_NAME =r"Project1"

def load_data():

    sample_data = {
        "Day": list(range(1, 31)),
        "Electricity_Usage": [
            120, 125, 130, 128, 135,
            138, 142, 145, 148, 150,
            155, 158, 160, 162, 165,
            168, 170, 172, 175, 178,
            180, 183, 185, 188, 190,
            193, 195, 198, 200, 203
        ]
    }


    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(sample_data)
        df.to_csv(FILE_NAME, index=False)
        print(" Sample file created.")
        return df

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        df = pd.DataFrame(sample_data)
        df.to_csv(FILE_NAME, index=False)
        print("File was empty. Sample data added.")

    return df


def save_data(df):
    df.to_csv(FILE_NAME, index=False)


def add_data():
    df = load_data()
    day = int(input("Enter Day: "))
    usage = float(input("Enter Electricity Usage: "))
    new_data = pd.DataFrame({
        "Day": [day],
        "Electricity_Usage": [usage]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df)
    print("Data Added Successfully.\n")


def update_data():
    df = load_data()

    if df.empty:
        print("No Data Available.\n")
        return

    print(df)

    day = int(input("Enter Day to Update: "))

    if day in df["Day"].values:
        usage = float(input("Enter New Usage: "))
        df.loc[df["Day"] == day, "Electricity_Usage"] = usage
        save_data(df)
        print("Data Updated Successfully.\n")
    else:
        print("Day Not Found.\n")


def delete_data():
    df = load_data()

    if df.empty:
        print("No Data Available.\n")
        return

    print(df)

    day = int(input("Enter Day to Delete: "))

    if day in df["Day"].values:
        df = df[df["Day"] != day]
        save_data(df)
        print("Data Deleted Successfully.\n")
    else:
        print("Day Not Found.\n")


def view_data():
    df = load_data()

    if df.empty:
        print("No Data Available.\n")
    else:
        print(df)
        print()


def predict_usage():
    df = load_data()

    if len(df) < 2:
        print("Not Enough Data for Prediction.\n")
        return

    X = df[["Day"]]
    y = df["Electricity_Usage"]

    model = LinearRegression()
    model.fit(X, y)

    future_day = int(input("Enter Future Day: "))
    future_data = pd.DataFrame({"Day": [future_day]})
    prediction = model.predict(future_data)

    print(f"Predicted Electricity Usage: {prediction[0]:.2f} Units\n")


while True:
    print("UTILITY USAGE PREDICTION TOOL")
    print("1. Add Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. View Data")
    print("5. Predict Usage")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_data()

        elif choice == 2:
            update_data()

        elif choice == 3:
            delete_data()

        elif choice == 4:
            view_data()

        elif choice == 5:
            predict_usage()

        elif choice == 6:
            print("Thank You")
            break

        else:
            print("Invalid Choice\n")

    except Exception as e:
        print("Error:", e)
        print()