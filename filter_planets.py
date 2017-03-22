import csv

filename = "planets.csv"
every_file = []

def filter_criteria(fdnames, rad, den, mas, src, dest):
    planet_radius = rad
    earth_radius = 0.091 #in jupiter radii

    planet_mass = mas
    earth_mass = 0.00315 #in terms of jupiters mass

    planet_density = den

    if ((planet_radius > (1.5*earth_radius) and planet_radius <= (2.5 * earth_radius))
        or (planet_mass>(5*earth_mass) and planet_mass<=(10*earth_mass))
        or (planet_density>=3.9 and planet_density<=6.5)):
        dest.append(src)
        pass
    pass

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    field_names = reader.fieldnames
    all_rows = []
    for row in reader:
        if row["pl_bmassj"] == "" or row["pl_radj"] == "" or row["pl_dens"] == "":
            pass
        else:
            radius = float(row["pl_radj"])
            mass = float(row["pl_bmassj"])
            density = float(row["pl_dens"])
            filter_criteria(field_names, radius, density, mass, row, all_rows)
            pass

        pass

    every_file = all_rows


    #create or update new csv file
    with open('cleaneddata.csv', 'w') as csvfilee:
        fieldnames = []
        writer = csv.DictWriter(csvfilee, fieldnames=field_names)
        writer.writeheader()
        for rw in every_file:
            writer.writerow(rw)
            pass

