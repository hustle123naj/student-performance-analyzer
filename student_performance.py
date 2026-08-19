import pandas as pd

data = {
    "Name": ["Asha", "Riya", "Asha", "Riya", "Neha", "Neha"],
    "Subject": ["Math", "Math", "Python", "Python", "Math", "Python"],
    "Marks": [80, 90, 85, 95, 70, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage marks of each student:")
print(df.groupby("Name")["Marks"].mean())

print("\nHighest marks of each student:")
print(df.groupby("Name")["Marks"].max())

print("\nTotal marks of each student:")
print(df.groupby("Name")["Marks"].sum())

print("\nStudent performance summary:")
print(df.groupby("Name")["Marks"].agg(["mean", "max", "min"]))