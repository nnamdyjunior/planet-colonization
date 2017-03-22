import csv
import math
import random


field_names = []
every_file = []
def findxy(dist, angle):
    x_cord = dist * math.cos(math.radians(angle))
    y_cord = dist * math.sin(math.radians(angle))

    return x_cord, y_cord
    pass

with open("cleaneddata.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    field_names = reader.fieldnames
    all_rows = []
    for row in reader:
        if row["st_dist"] == "" or row["pl_orbincl"] == "":
            if row["st_dist"] == "":
                row["st_dist"] = random.uniform(12.04, 2119)
            if row["pl_orbincl"] == "":
                row["pl_orbincl"] = random.uniform(15, 90.76)
            distance = float(row["st_dist"])
            angle = float(row["pl_orbincl"])
            xx, yy = findxy(distance, angle)
            row['X'] = xx
            row['Y'] = yy
            all_rows.append(row)
            pass
        else:
            distance = float(row["st_dist"])
            angle = float(row["pl_orbincl"])
            xx, yy = findxy(distance, angle)
            row['X'] = xx
            row['Y'] = yy
            all_rows.append(row)
            pass
    every_file = all_rows

with open('finaldata.csv', 'w') as csvfilee:
    # fieldnames = []
    writer = csv.DictWriter(csvfilee, fieldnames=field_names + ['X', 'Y'])
    writer.writeheader()
    for rw in every_file:
        writer.writerow(rw)
        pass