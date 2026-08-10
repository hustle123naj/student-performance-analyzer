import matplotlib.pyplot as plt

students = ["A" , "B" , "C","D","E"]
marks = [85, 72, 90, 65, 78]
studyhours = [5, 3, 6, 2, 4]

plt.bar(students , marks)
plt.title("student marks")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()

plt.scatter(studyhours,marks)
plt.xlabel("studyhours")
plt.ylabel("marks")
plt.title("studyhours vs marks")
plt.grid()
plt.show()

plt.hist(marks)
plt.title("marks distribution")
plt.xlabel("marks")
plt.ylabel("no of students")
plt.show()

plt.pie(marks , labels = students , autopct = "%1.1f%%")
plt.title("marks contribution")
plt.show()