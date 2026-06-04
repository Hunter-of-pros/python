import csv
data = {}
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for key in row:
            data.setdefault(key, []).append(float(row[key]))
for col, values in data.items():
    print("\nColumn:", col)
    print("Max:", max(values))
    print("Min:", min(values))
    print("Average:", sum(values)/len(values))