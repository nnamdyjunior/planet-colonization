import csv
import math
import random


field_names = []
every_file = []
def findxy(tem, den):
    temp = tem / 5772
    dens = den / 5.5
    x_cord = temp
    y_cord = dens

    return x_cord, y_cord
    pass

with open("finaldata.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    field_names = reader.fieldnames
    all_rows = []
    for row in reader:
        if row["st_teff"] == "" or row["pl_dens"] == "":
            if row["st_teff"] == "":
                row["st_teff"] = random.uniform(3170, 6475)
            if row["pl_dens"] == "":
                row["pl_dens"] = random.uniform(0, 77.7)
            temp = float(row["st_teff"])
            dens = float(row["pl_dens"])
            xx, yy = findxy(temp, dens)
            row['X'] = xx
            row['Y'] = yy
            all_rows.append(row)
            pass
        else:
            temp = float(row["st_teff"])
            dens = float(row["pl_dens"])
            xx, yy = findxy(temp, dens)
            row['Energy'] = xx
            row['Metallicity'] = yy
            all_rows.append(row)
            pass
    every_file = all_rows

with open('newfinaldata.csv', 'w') as csvfilee:
    # fieldnames = []
    writer = csv.DictWriter(csvfilee, fieldnames=field_names + ['Energy', 'Metallicity'])
    writer.writeheader()
    for rw in every_file:
        writer.writerow(rw)
        pass