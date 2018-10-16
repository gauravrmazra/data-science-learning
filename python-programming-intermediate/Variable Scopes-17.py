## 1. The Data Set ##

print(len(borrower_default_count_240))
print(borrower_default_count_240[0:10])
print(institution)
print(city)
print(state)


## 2. Built-In Functions ##

total = sum([6, 11])

## 3. Overwriting a Built-In Function ##

sum = sum(borrower_default_count_240)
# Run the code, and then uncomment the bottom
# line to see the result.
#test = sum(principal_outstanding_240)
print(sum)

## 4. Scopes ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
print(total)
average = find_average(principal_outstanding_240)
print(total)

## 5. Scope Isolation ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)

print(length)

average = find_average(principal_outstanding_240)

principal_length = find_length(principal_outstanding_240)

print(length)

## 6. Scope Inheritance ##

def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    print('global length=', length, ', length=', len(column))
    return total / length

length = 10

average = find_average(principal_outstanding_240)

## 7. Inheritance Limits ##

total = 10

def find_total(column):
    #total = total + sum(column)
    return total

print(find_total(principal_outstanding_240))

## 9. Global Variables ##

def global_variable():
    global b
    b = 20

global_variable()

print(b)