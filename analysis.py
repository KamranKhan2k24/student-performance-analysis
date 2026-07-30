import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\91919\OneDrive\Desktop\student_performance_dataset.csv")
print(df.head())

print(df.info())
print(df.shape)
print(df.columns)
print("Shape",df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())

print("Average Math",df["Math"].mean())
print("Average Science",df["Science"].mean())
print("Average English",df["English"].mean())

print("Highest Math",df["Math"].max())
print("Highest Science",df["Science"].max())
print("Highest English",df["English"].max())

print("Lowest Math",df["Math"].min())
print("Lowest Science",df["Science"].min())
print("Lowest English",df["English"].min())

print("The average Attendence",df["Attendance"].mean())
print("The highest Attendence",df["Attendance"].max())
print("The lowest Attendence",df["Attendance"].min())

df["Total"]=df["Math"]+df["Science"]+df["English"]
print(df.head())

df["Average"]=df["Total"]/3
print(df.head())

topper=df.sort_values(by="Total",ascending=False)
print(topper.head())

weak_student = df[df["Math"] < 40]
print(weak_student)

good_attendence = df[df["Attendance"] > 90]
print(good_attendence)

plt.figure(figsize=(10,5))
plt.bar(df["Name"],df["Math"])
plt.title("Math Scores of Students")
plt.xlabel("Students")
plt.ylabel("Math Marks")

plt.xticks(rotation=45)

plt.show()

plt.figure(figsize=(8,5))

plt.hist(df["Science"],bins=5)

plt.title("Distribution of Science Scores")
plt.xlabel("Science Marks")
plt.ylabel("Number of Students")

plt.show()

gender_counts = df["Gender"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()

print(df[["Math","Science","English"]].corr())

df.to_csv("student_performance_analysis.csv", index=False)