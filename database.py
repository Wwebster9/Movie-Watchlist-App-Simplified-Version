import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

CREATE_MOVIES_TABLE = """
    CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT
);"""

CREATE_WATCHED_TABLE = """
    CREATE TABLE IF NOT EXISTS watched (
    movie_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title) VALUES (%s);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_WATCHED_MOVIES = """
    SELECT movies.* FROM movies
    JOIN watched ON movies.id = watched.movie_id;
"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (movie_id) VALUES (%s);"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title ilike %s;"

connection = psycopg2.connect(os.environ["DATABASE_URL"])


def create_tables():
    """Creates the new tables in the SQL database and creates an index on the movies table"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)


def add_movie(title):
    """Adds a new movie to the movies table"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title,))


# def delete_movie(movie_id):
#     """Deletes a selected movie from the movies table"""
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(DELETE_MOVIES, (movie_id,))


def get_movies():
    """Grabs all movies from the movies table"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def search_movies(search_term):
    """
    Allows the user to search the movies table
    :param search_term: Search keywords (e.g., portion of a movie title)
    :return: Cursor pointing to the first row returned
    """
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
            return cursor.fetchall()


def watch_movie(movie_id):
    """Inserts a movie into the watched table"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (movie_id,))


def get_watched_movies():
    """Runs SQL query to grab the watched movies table"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES)
            return cursor.fetchall()
