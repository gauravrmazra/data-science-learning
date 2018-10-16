## 2. Sets ##

gender = []
for legislator in legislators:
    gender.append(legislator[3])

gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []

for legislator in legislators:
    party.append(legislator[6])
    
party = set(party)
    
print(party)
print(legislators)

## 4. Missing Values ##

for legislator in legislators:
    if legislator[3] == '':
        legislator[3] = 'M'
        

## 5. Parsing Birth Years ##

birth_years = []

for legislator in legislators:
    birthday = legislator[2]
    parts = birthday.split('-')
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    fh = float('hello')
except Exception:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as ex:
    print(type(ex))
    print(ex)

## 8. The Pass Keyword ##

converted_years = []

for year in birth_years:
    try:
        converted_years.append(int(year))
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##

for legislator in legislators:
    parts = legislator[2].split('-')
    try:
        birth_year = int(parts[0])
    except Exception:
        birth_year = 0
    
    legislator.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
        
    last_value = row[7]