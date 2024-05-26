# import csv

# #@todo, save all possible ratings uppercased
# #@todo, save genres uppercased

# # This function will parse the CSV
# # depending if it is thre streaming service or the large data set, it will create a certain dictionary
# # input: file path name adn streaming service (if it is empty string, then it is one of our core data sets)
# # output: array of dictionaries that are filled with movies and their information
# def ingestMoviesFromCSV(fileName, streamingService):
#     data = [] # this is the array of dictionaries we will send back
#     # keeps track of what indexes
#     # keeps track of the header and the corresponding index. -1 represents non existent in the data
#     headerDict = {"image":-1, "year": -1, "name": -1, "genre": -1, "plot": -1, "type": -1, "rating": -1}
#     with open(fileName) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         encounteredHeader = False # keeps track if we encountered the header or not.  if we didn't, we need to save the index of the information we want to save
#         for row in csv_reader:
#             rowData = {} # will store the data we want to save from the row
#             if encounteredHeader:
#                 # will save to a dictionary
#                 if streamingService.replace(" ","") == "":
#                     # this is the IMDB data set
#                     # will only add the row's data if the movie name exists and the image exists
#                     if headerDict["name"] != -1 and headerDict["image"] != -1:
#                         rowData.update({"name": row[headerDict["name"]]})
#                         rowData.update({"image": row[headerDict["image"]]})
#                 else:
#                     # this is our streaming service dataset
#                     # we don't need to check if the header doesn't exist (or if the corresponding index is -1) because it is a guarentee it exists
#                     # will only save movies
#                     if (row != [] and row[headerDict["type"]].lower().replace(" ","") == "movie"):
#                         # iterates through all keys in the header dictionary to retrieve the corresponding index
#                         for key in headerDict:
#                             # will not add type, image, or if value is -1 (would result in out of bounds)
#                             if key != "image" and key != "type" and headerDict[key] != -1:
#                                 value = row[headerDict[key]].strip(u'\u200b')
#                                 if key == "genre" or key == "rating":
#                                     value = value.upper()
#                                 rowData.update({key: value})
#                         if len(rowData) > 0:
#                             # since we know there was data in the row, we can add the streaming service
#                             rowData.update({"streamingService": streamingService})
#                 # will only append the row to the data we are sending only if the name is saved
#                 if "name" in rowData:
#                     data.append(rowData)
#             else:
#                 # will find the index for each corresponding header
#                 # save the index so know later on which index to parse
#                 headerIndex = 0 
#                 for header in row:
#                     headerCompare = header.lower().replace(" ","") 
#                     # based on what was in the titles of the csvs, would take into acount how to save into our headersDict by saving hte index of where they are located
#                     if "poster" in headerCompare:
#                         headerDict["image"] = headerIndex
#                     elif "year" in headerCompare:
#                         headerDict["year"] = headerIndex
#                     elif "genre" in headerCompare:
#                         headerDict["genre"] = headerIndex
#                     elif "name" in headerCompare or "title" in headerCompare:
#                         headerDict["name"] = headerIndex
#                     elif "plot" in headerCompare or "overview" in headerCompare or "description" in headerCompare:
#                         headerDict["plot"] = headerIndex
#                     elif "type" in headerCompare:
#                         headerDict["type"] = headerIndex
#                     elif "rating" in headerCompare or "rated" in headerCompare:
#                         headerDict["rating"] = headerIndex
#                     headerIndex+=1
#             encounteredHeader = True #toggles to true since we have viewed it
#     return data

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv, json
from  dotenv import load_dotenv
import os

load_dotenv()

def build_db(imdb, netflix1, amazon1, hulu1, disney1):
    movies = []
    netflix = []
    amazon = []
    hulu = []
    disney = []
    if netflix1 != "":
        with open(netflix1, "r") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                netflix.append(row)

    if amazon1 != "":
        with open(amazon1, "r") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                amazon.append(row)

    if hulu1 != "":
        print(hulu1)
        with open(hulu1, "r") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                hulu.append(row)

    if disney1 != "":
        with open(disney1, "r") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                disney.append(row)
    
    with open(imdb, "r") as mov:
        reader = csv.DictReader(mov, delimiter=',')
        for row in reader:
            streaming = []
            exists = [element for element in netflix if element['title'] == row['Series_Title']]
            if exists:
                streaming.append('Netflix')
            exists = [element for element in amazon if element['title'] == row['Series_Title']]
            if exists:
                streaming.append('Amazon')
            exists = [element for element in hulu if element['title'] == row['Series_Title']]
            if exists:
                streaming.append('Hulu')
            exists = [element for element in disney if element['title'] == row['Series_Title']]
            if exists:
                streaming.append('Disney')
            streaming.append('Illegal')
            row['streaming'] = streaming
            movies.append(row)
        with open('movie.json', 'w', encoding='utf-8') as jsonf:
            json_string = json.dumps(movies, indent=4)
            jsonf.write(json_string)
    return movies


def upload_firebase(data):
    connection_string = json.loads(os.getenv('FIREBASE_AUTHENTICATION'))
    cred = credentials.Certificate(connection_string)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://filmfinder-5145d-default-rtdb.firebaseio.com/',
        }
    )

    ref = db.reference('/')
    ref.set({
        "Movies_test": data
    })



if __name__ == "__main__":
    imdb = "data_sets/imdb_top_1000.csv"
    netflix = "data_sets/netflix_titles.csv"
    amazon = "data_sets/amazon_prime_titles.csv"
    hulu = "data_sets/hulu_titles.csv"
    disney = "data_sets/disney_plus_shows.csv"

    data = build_db(imdb, netflix, amazon, hulu, disney)
    upload_firebase(data)