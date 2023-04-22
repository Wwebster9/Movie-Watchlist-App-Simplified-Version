import database

menu = """Please select one of the following options:
1) Add new movie.
2) View all movies.
3) Watch a movie.
4) View watched movies.
5) Search for a movie.
6) Exit.

Your selection: """
welcome = "\nWelcome to the movie watchlist app!"


# print welcome message and create empty tables
print(welcome)
database.create_tables()


def prompt_add_movies():
    title = input("Movie title: ")
    database.add_movie(title)


def print_movie_list(heading, movie_list):
    print(f"\n----- {heading} movies -----\n")
    # _id used because id is a built-in function and don't want to overwrite that function
    for _id, title in movie_list:
        print(f"{_id}: {title}")
    print("\n----- End of list -----\n")


def prompt_watch_movie():
    movie_id = input("Enter the Movie ID: ")
    database.watch_movie(movie_id)


def prompt_show_watched_movies():
    watched_movies = database.get_watched_movies()
    if movies:
        print_movie_list("Watched", watched_movies)
    else:
        print("\nNo watched movies\n")


def prompt_search_movies():
    search_term = input("Enter your search term: ")
    searched_movies = database.search_movies(search_term)
    if searched_movies:
        print_movie_list("Found", searched_movies)
    else:
        print("\nNo movies found for that search term\n")


# def prompt_delete_movie():
#     movie_id = input("Enter the Movie ID of the movie you would like to delete from the above list: ")
#     database.delete_movie(movie_id)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movies()
    elif user_input == "2":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
        prompt_watch_movie()
    elif user_input == "4":
        prompt_show_watched_movies()
    elif user_input == "5":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
