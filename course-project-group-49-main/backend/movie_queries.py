import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
import csv, json
from dotenv import load_dotenv
import os 
import collections
load_dotenv()

class MovieQueries:
    def __init__(self):
        # connects to firebase
        connection_string = json.loads(os.getenv('FIREBASE_AUTHENTICATION'))
        cred = credentials.Certificate(connection_string)
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://filmfinder-5145d-default-rtdb.firebaseio.com/',
                }
            )

    # ideally, we will use this when we click (not for search)
    def get_movie_by_streaming_service(self, streamingService):
        
        # this is the query to retrieve the movie
        # compares if the streaming matches the streaming service we sent
        # right now it is case sensitive
        ref = db.reference('/Movies')
        movie_dict = ref.get()
        lst = []
        for m in movie_dict:
            if streamingService in m["streaming"]:
                lst.append(m)
        return lst

    def get_movie_by_genre(self, genre):
        
        # this is the query to retrieve the movie
        # compares if the streaming matches the streaming service we sent
        # right now it is case sensitive
        ref = db.reference('/Movies')
        movie_dict = ref.get()
        lst = []
        for m in movie_dict:
            genre_lst = m["Genre"].split(",")
            if genre in genre_lst:
                lst.append(m)
        return lst

    # ideally, we will use this when we click (not for search)
    def get_movie(self, movie):
        # this is the query to retrieve the movie
        # compares if the series title matches the movie we found in the movies collection
        # right now it is case sensitive
        ref = db.reference('/Movies')
        movie_dict = ref.get()
        for m in movie_dict:
            if m["Series_Title"] == movie:
                return m


    def delete_movie(self, movie):
        # this is the query to retrieve the movie
        # compares if the series title matches the movie we found in the movies collection
        # right now it is case sensitive
        ref = db.reference('/Movies')
        movie_dict = ref.get()
        print(movie_dict)
        for key,value in movie_dict:
            # print(key)
            if value["Series_Title"] == movie:
                print(value["Series_Title"])