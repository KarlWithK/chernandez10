#!/usr/bin/env python
import csv
from random import choices

occupations = {} # initialize the dictionary
with open("./data/occupations.csv", "r", newline='') as csv_file:
    # we are lazy so we used the csv library
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if not (row[0] == "Job Class" or row[0] == "Total"): # skip over lines
            occupations[row[0]] = float(row[1]) # populated the dictionary


# only have to assign once
key = list(occupations.keys())
values = list(occupations.values())

def get_all_jobs() -> list:
    return key

def get_occupations() -> tuple:
    # we found that you had to zip to create a tuple so
    # jinja can iterate through each list
    return zip(key, values)


def get_random_occupations() -> str:
    return choices(key, values, k=1)[0]


if __name__ == "__main__":
    print(get_random_occupations())
