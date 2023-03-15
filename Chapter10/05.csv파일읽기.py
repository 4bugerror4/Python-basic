import csv

file = open("./Chapter10/student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)

for d in reader:
    print(d)

file.close()
