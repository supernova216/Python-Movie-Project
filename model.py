"""Models for movie ratings app."""
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    # ratings table also connected

    def __repr__(self):
         return f"<User user_id = {self.user_id} email = {self.email}>"
    
class Movie(db.Model):

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String, unique = True)
    overview = db.Column(db.Text, unique = True)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String, unique = True)

    # ratings table also connected

    def __repr__(self):
         return f"<Movie movie_id = {self.movie_id} title = {self.title}>"
    
class Rating(db.Model):
     
     __tablename__ = "ratings"

     rating_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
     score = db.Column(db.Integer)
     movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"), nullable = False)
     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

     movie = db.relationship("Movie", backref = "ratings")
     user = db.relationship("User", backref = "ratings")

     def __repr__(self):
        return f"<Rating rating_id = {self.rating_id} score = {self.score}>"

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=False):
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        flask_app.config["SQLALCHEMY_ECHO"] = echo
        flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        
        db.app = flask_app
        db.init_app(flask_app)

        print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
