#!/usr/bin/env python
# Carlos "Karl" Hernandez
# SoftDev
# K05 -- Aim: started to use python in softdev
# 2020-09-30

# Line above is just to make sure you don't need the .py extension
# Made by William Li, May Hathaway, and Carlos "Karl" Hernandez
from random import choice

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

def get_random_name():
    print("Team name: orpheus, rex, endymion!\n")
    name = input("Enter a team:\n").lower()
    while name not in KREWES:
        name = input("Please enter a correct team:\n").lower()
    team = KREWES[name]
    print(choice(team))


if __name__ == "__main__":
    get_random_name()
