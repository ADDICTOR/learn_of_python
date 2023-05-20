import csv

filename = "../source/example.csv"

with open(filename, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)

for row in csvreader:
    print(row)