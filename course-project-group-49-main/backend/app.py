from flask import Flask, request, jsonify, session, render_template, redirect
import pyrebase
from movie_queries import MovieQueries
import firebase_admin 
from firebase_admin import credentials
import json
import os 
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/')
def hello():
    return jsonify({'Message': "Welcome to FilmFinder"})

# connection_string = json.loads(os.getenv('FIREBASE_AUTHENTICATION'))
# cred = credentials.Certificate(connection_string)
# firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://filmfinder-5145d-default-rtdb.firebaseio.com/',
#         }
# )

# firebase = pyrebase.initialize_app(cred)
# auth = firebase.auth()

# @app.route('/', methods = ['POST', 'GET'])
# def index():
#     if('user' in session):
#         return 'Hi, {}'.format(session['user'])
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         try:
#             user = auth.sign_in_with_email_and_password(email,password)
#             session['user'] = email
#         except:
#             return 'Failed to login'
#     return render_template('home.html') #name of the file which displays the authentication 

# @app.route('/logout')
# def logout():
#     session.pop('user')
#     return redirect('/')

@app.route('/search_by_streaming_service', methods=['GET'])
def search_by_streaming_service():
    streaming = request.args.get('streaming')
    records = MovieQueries().get_movie_by_streaming_service(streaming)
    response = jsonify({'movies': records})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

@app.route('/movie_details', methods=['GET'])
def search_by_name():
    name = request.args.get('name')
    details = MovieQueries().get_movie(name)
    response = jsonify({'movies': details})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

@app.route('/search_by_genre', methods=['GET'])
def search_by_genre():
    genre = request.args.get('genre')
    records = MovieQueries().get_movie_by_genre(genre)
    response = jsonify({'movies': records})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

app.run(debug = True)