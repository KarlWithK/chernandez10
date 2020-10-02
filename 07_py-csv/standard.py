#!/usr/bin/env python
# Carlos "Karl" Hernandez
# SoftDev
# K07 -- Aim: Worked with standard io in python
# 2020-09-30
# Team TLK: Matthew Hui, Yi Ling Wu, and Carlos "Karl" Hernandez
import csv
from random import choices


def get_random_occupations():
    # need to open file
    with open("./occupations.csv", "r", newline='') as csv_file:
        # we are lazy so we used the csv library
        reader = csv.reader(csv_file, delimiter=',')
        occupations = {} # initialize the dictionary
        for row in reader:
            if not (row[0] == "Job Class" or row[0] == "Total"): # skip over lines
                occupations[row[0]] = float(row[1]) # populated the dictionary
        # next two lines are so we can use random.choices()
        key = list(occupations.keys())
        values = list(occupations.values())
        return choices(key, values, k=1)[0]


if __name__ == "__main__":
    print(get_random_occupations())
