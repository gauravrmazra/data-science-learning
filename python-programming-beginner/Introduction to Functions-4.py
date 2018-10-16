## 1. Overview ##

f = open("movie_metadata.csv", "r")
rows = f.read().split("\n")
movie_data = []

for row in rows:
    movie_data.append(row.split(','))

print(movie_data[0:5])

## 3. Writing Our Own Functions ##

def first_elts(movies):
    movie_names = []
    for movie in movies:
        movie_names.append(movie[0])
    return movie_names

movie_names = first_elts(movie_data)

print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[6] == 'USA':
        return True
    else:
        return False

wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equals_str(input_lst, index, input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

wonder_woman_in_color = index_equals_str(wonder_woman, 2, "Color")

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(movies, input_str, index, header_row = False):
    count = 0
    if header_row == True:
        movies = movies[1:]
    
    for movie in movies:
        if movie[index] == input_str:
            count = count + 1
    
    return count;

num_of_us_movies = feature_counter(movie_data, "USA", 6, header_row=True)
    

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(movies):
    num_japan_films = feature_counter(movies, 6, "Japan", header_row=True)
    num_color_films = feature_counter(movies, 2, "Color", header_row=True)
    num_films_in_english = feature_counter(movies, 5, "English", header_row=True)
    m = {'japan_films' : num_japan_films, 'color_films': num_color_films, 'films_in_english': num_films_in_english}
    return m

summary = summary_statistics(movie_data)