"""
Name: Kazuki Pickersgill
Date started: 16-10-2022
GitHub URL:https://github.com/KazukiPJCU/starter_a1_movies/blob/main/assignment1.py
"""

from sys import exit

FILENAME = "movies.csv"
CATEGORIES = "Action", "Comedy", "Documentary", "Drama", "Thriller"


def main():
    """Prints intro"""
    print("Movies To Watch 1.0 - by Kazuki Pickersgill")
    movies = get_movies_file()

    while True:
        display_menu()  # Displays menu
        menu_choice = input(">>> ").upper()
        if menu_choice == "D":
            print("Display Movies")
            display_movies(movies)
        elif menu_choice == "A":
            print("Add movies")
            add_to_movies_list(movies)
        elif menu_choice == "W":
            print("Watch a movie")
            check_watched(movies)
        elif menu_choice == "Q":
            print(movies)
            print("{} movies saved to movies.csv\nEnjoy Your day!".format(len(movies)))
            save_to_file(movies)
            exit()
        else:
            print("Invalid Menu choice")


def check_watched(movies):
    """Checks if there are any movies left to watch"""
    watched_movies = 0
    unwatched_movies = 0
    for movie in movies:
        parts = movie.split(",")
        if "u" in parts[3]:
            unwatched_movies += 1  # Counts unwatched movies
        elif "w" in parts[3]:
            watched_movies += 1
    if unwatched_movies == 0:
        print("No more movies to watch")
    else:
        watch(movies)  # If there are movies to watch continues to watch(movies) method


def add_to_movies_list(movies):
    """Add movie to movies list"""

    movie_title = input("Movie Title: ")
    while movie_title == "":
        print("Title can not be black")
        movie_title = input("Movie Title: ")
    movie_year = check_movie_year()
    movie_category = check_movie_category()
    add_movie = ("{}, {}, {}, u".format(movie_title, movie_year, movie_category))
    movies.append(add_movie)
    print("{} ({} from {}) added to movie list".format(movie_title, movie_category, movie_year))


def check_movie_category():
    """Checks if movie category is in the set of available categories"""
    print("Categories Available: ", end='')
    print(', '.join(CATEGORIES))
    movie_category = input("Category: ").title()
    while movie_category == "":
        print("Category can not be blank")
        movie_category = input("Category: ")
    if movie_category not in CATEGORIES:
        print("Invalid category; using Other")
        movie_category = "other"
    return movie_category


def check_movie_year():
    """Checks movie year input is valid"""
    while True:
        try:
            movie_year = int(input("Year: "))
            while movie_year < 0:
                print("Number must be greater than 0")
                movie_year = int(input("Year: "))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            break
    return movie_year


def save_to_file(movies):
    """Saves movies in csv file"""
    with open(FILENAME, 'w') as f:
        for movie in movies:
            f.write("%s" % movie)


def display_menu():
    """prints Menu"""
    print("Menu:\nD - Display movies\nA - Add new movies\nW - Watch movie\nQ - Quit")


def get_movies_file():
    """Opens and closes movie text file & displays how many movies loaded"""
    input_file = open(FILENAME, "r")
    movies = input_file.readlines()
    print('{} movies loaded from {}'.format(len(movies), FILENAME))
    input_file.close()
    return movies


def display_movies(movies):
    """Display movies into rows"""
    movie_list = 1
    watched_movies = 0
    unwatched_movies = 0
    for movie in movies:
        parts = movie.split(",")
        print(movie_list, end=" ")
        if "u" in parts[3]:
            unwatched_movies += 1  # Counts unwatched movies
            print("* ", end=" ")
        elif "w" in parts[3]:
            watched_movies += 1
            print("  ", end=" ")
        print(("{:<{}} - {:<{}} ({})".format(parts[0], movie_name_format(movies), parts[1], movie_year_format(movies),
                                             parts[2])))
        movie_list += 1
    print('{0} Movies watched, {1} Movies still to watch'.format(watched_movies, unwatched_movies))


def movie_year_format(movies):
    """Gets the longest element in movie year for formatting"""
    max_length = 0
    for movie in movies:
        parts = movie.split(",")
        if max_length < len(parts[1]):
            max_length = len(parts[1])
        else:
            continue
    return max_length


def movie_name_format(movies):
    """Gets the longest element in movie name for formatting"""
    max_length = 0
    for movie in movies:
        parts = movie.split(",")
        if max_length < len(parts[0]):
            max_length = len(parts[0])
        else:
            continue
    return max_length


def watch(movies):
    """Marks movie as watched"""
    while True:
        try:
            enter_movie_num = int(input("Enter the number of a movie to mark as watched\n>>> "))
            while enter_movie_num < 0:
                print("Number must be >= 1")
                enter_movie_num = int(input(">>> "))
            while enter_movie_num not in range(1, len(movies) + 1):  # checks if number is in the range of movies list
                print("Invalid movie number")
                enter_movie_num = int(input(">>> "))
            movie = movies[enter_movie_num - 1].split(",")
            if "u" in movie[3]:  # checks if movie selected is unwatched
                movie[3] = movie[3].replace("u", "w")  # replace unwatched with watched
                movies[enter_movie_num - 1] = ",".join(movie)  # adds movie back to list
                print("{} from {} watched".format(movie[0], movie[1]))
                return movies
            else:
                print("You have already watched {}".format(movie[0]))
                return movies
        except IndexError:
            print("Invalid movie number")
        except ValueError:
            print("Invalid input; enter a valid number")


main()
