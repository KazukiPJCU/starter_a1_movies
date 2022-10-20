"""
Name: Kazuki Pickersgill
Date started: 16-10-2022
GitHub URL:
"""


def main():
    """Prints intro"""
    print("Movies To Watch 1.0 - by Kazuki Pickersgill")
    input_file, movies = get_movies_file()

    while True:
        display_menu()
        choice = input(">>> ").upper()
        if choice == "D":
            print("Display Movies")
            display_movies(movies)
        elif choice == "A":
            print("Add movies")
        elif choice == "W":
            print("Watch a movie")
        elif choice == "Q":
            print("{} movies saved to movies.csv\nEnjoy Your day!".format(len(movies)))
            return False
        else:
            print("Invalid choice")
            display_menu()
            choice = input(">>> ").upper()


def display_menu():
    """prints Menu"""
    print("Menu:\nD - Display movies\nA - Add new movies\nW - Watch movie\nQ - Quit")


def get_movies_file():
    """Opens and closes movie text file & displays how many movies loaded"""
    input_file = open("movies.csv", "r")
    movies = input_file.readlines()
    print('{} movies loaded'.format(len(movies)))
    input_file.close()
    return input_file, movies


if __name__ == '__main__':
    main()
