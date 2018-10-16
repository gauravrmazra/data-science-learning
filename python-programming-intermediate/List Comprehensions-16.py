## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]


for idx, ship in enumerate(ships):
    print(ship)
    print(cars[idx])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for idx, row in enumerate(things):
    row.append(trees[idx])
    

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2 * apple_price for apple_price in apple_prices]

apple_prices_lowered = [apple_price-100 for apple_price in apple_prices]

## 5. Counting Female Names ##

def getYear(birthdate):
    parts = birthdate.split('-')
    if len(parts) == 3:
        return int(parts[0])
    else:
        return None

name_counts = {}

for legislator in legislators:
    
    year = getYear(legislator[2])
    if year is not None and year > 1940 and legislator[3] == 'F':
        if legislator[1] in name_counts:
            name_counts[legislator[1]] = name_counts[legislator[1]] + 1
        else:
            name_counts[legislator[1]] = 1


## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for value in values:
    result = value is not None and value > 30
    checks.append(result)

## 8. Highest Female Name Count ##

max_value = None
for name in name_counts:
    count = name_counts[name]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = [ name for name, count in name_counts.items() if count == 2]

## 11. Finding the Most Common Male Names ##

def getYear(birthdate):
    parts = birthdate.split('-')
    if len(parts) == 3:
        return int(parts[0])
    
    return None

male_name_counts = {}

for legislator in legislators:
    year = getYear(legislator[2])
    if year is not None and year > 1940 and legislator[3] == 'M':
        if legislator[1] in male_name_counts:
            male_name_counts[legislator[1]] = male_name_counts[legislator[1]] + 1
        else:
            male_name_counts[legislator[1]] = 1

highest_male_count = None

for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count


top_male_names = [name for name, count in male_name_counts.items() if count == highest_male_count]
