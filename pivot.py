import pandas as pd

data = {
    "Name": ["Asha", "Asha", "Riya", "Riya", "Neha", "Neha"],
    "Subject": ["Math", "Python", "Math", "Python", "Math", "Python"],
    "Marks": [80, 90, 85, 95, 70, 88]
}

df = pd.DataFrame(data)
print(df)

pivot = df.pivot_table(
    values = "Marks",
    index = "Name",
    columns = "Subject",
    aggfunc = "max"
)
print(pivot)