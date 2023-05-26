''' This module is reponsible for Create Read Update Delete operations in our Postgres database'''
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):  
    """Create and return a new user."""

    new_user = User(email=email, password=password)

    return new_user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    new_movie = Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

    return new_movie

def get_movies():
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)

def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_rating(user, movie, score):
    """ Create and return a new rating"""

    new_rating = Rating(user = user, movie = movie, score = score)

    return new_rating

def get_user_by_email(email):
    '''Query a user by email'''
    return User.query.filter(User.email == email).first() 

def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """
    rating = Rating.query.get(rating_id)
    rating.score = new_score


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
