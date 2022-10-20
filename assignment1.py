"""
Name: Kazuki Pickersgill
Date started: 16-10-2022
GitHub URL:
"""
import csv
from sys import exit


def main():
    """Prints intro"""
    print("Movies To Watch 1.0 - by Kazuki Pickersgill")
    movies = get_movies_file()

    while True:
        display_menu()
        menu_choice = input(">>> ").upper()
        if menu_choice == "D":
            print("Display Movies")
            display_movies(movies)
        elif menu_choice == "A":
            print("Add movies")
        elif menu_choice == "W":
            print("Watch a movie")
        elif menu_choice == "Q":
            print(movies)
            print("{} movies saved to movies.csv\nEnjoy Your day!".format(len(movies)))
            with open("movies.csv", "w", newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerows([movies])
            exit()
        else:
            print("Invalid choice")
            display_menu()
            menu_choice = input(">>> ").upper()


def display_menu():
    """prints Menu"""
    print("Menu:\nD - Display movies\nA - Add new movies\nW - Watch movie\nQ - Quit")


def get_movies_file():
    """Opens and closes movie text file & displays how many movies loaded"""
    input_file = open("movies.csv", "r")
    movies = input_file.readlines()
    print('{} movies loaded'.format(len(movies)))
    input_file.close()
    return movies


def display_movies(movies):
    movie_list = 1
    watched_movies = 0
    unwatched_movies = 0
    for movie in movies:
        parts = movie.split(",")
        print(movie_list, end=" ")
        if "u" in parts[3]:
            unwatched_movies += 1
            print("*", end=" ")
        elif "w" in parts[3]:
            watched_movies += 1
            print("  ", end=" ")
        print(parts[0], end=format_movies(movies, parts[0]))
        print(" - {0} ({1})".format(parts[1], parts[2]))
        movie_list += 1
    print('{0} Movies watched, {1} Movies still to watch'.format(watched_movies, unwatched_movies))


def format_movies(movies, name_of_movie):
    max_length = 0
    space = ''
    for movie in movies:
        elements = movie.split(",")
        for element in elements:
            if max_length < len(element):
                max_length = len(element)
            else:
                continue
    for i in range(max_length - len(name_of_movie)):
        space += " "
    return space


if __name__ == '__main__':
    main()
