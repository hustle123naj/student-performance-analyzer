import pandas as pd

data = {
    "Name": ["Aisha", "Anu", "Rahul", "Sara", "Nikhil"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Marks": [85, 72, 95, 68, 80]
}

df = pd.DataFrame(data)
print(df.iloc[0:3])
print(df[["Name","Marks"]])
print(df[df["Marks"]>80])
df["marks_10"] = df["Marks"]/10
df = print(df.sort_values("Marks", ascending = False))
print(df)