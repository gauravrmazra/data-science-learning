## 2. Introduction to the Data ##

import csv

with open('nfl_suspensions_data.csv') as nfl:
    csvreader = csv.reader(nfl)
    nfl_suspensions = list(csvreader)
    print(nfl_suspensions[0])
    nfl_suspensions = nfl_suspensions[1:]
    years = {}
    for nfl_suspension in nfl_suspensions:
        if nfl_suspension[5] in years:
            years[nfl_suspension[5]] = years[nfl_suspension[5]] + 1
        else:
            years[nfl_suspension[5]] = 1
    print(years)
    

## 3. Unique Values ##

unique_teams = set([row[1] for row in nfl_suspensions])
unique_games = set([row[2] for row in nfl_suspensions])
print(unique_teams)
print(unique_games)

## 4. Suspension Class ##

class Suspension:
    def __init__(self, nfl_suspension):
        self.name = nfl_suspension[0]
        self.team = nfl_suspension[1]
        self.games = nfl_suspension[2]
        self.year = nfl_suspension[5]
        
        
third_suspension = Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return self.year

missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()