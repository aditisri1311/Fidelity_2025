import csv
with open("data.csv", "w", newline = "") as f:
    w = csv.writer(f)
    w.writerow(["Aditi", "Riddhi", "Anshika"])
    w.writerow(["Dikhya", "Ritika", 1])
f =open("data.csv","r")
r = csv.reader(f)
data  = list(r)
print(data)