# Pitch

With streaming services growing more popular every day, people have too many options and tend to struggle to pick a movie to watch. FilmFinder will allow users to find movie recommendations based on their available streaming services and their own interests.

We split our team into two groups: frontend (Diya & Shreya) and backend (Megan & Anushka). We plan to have two people work on the backend team because no one in our group has experience with databases. 

# Functionality

1. Users will be able to find recommendations for movies based on selected interests.
2. Users will be able to select streaming services of their choice and see movies provided by the service.
3. When selected, movies will display a synopsis, poster, and ratings, along with their streaming service and genre.

# Components

## Frontend
-   We worked with React because it allowed our website to be more dynamic since we can reuse components. We also used Node.js to complete the frontend of our project.
-   We have four page formats: a home page, a page that shows the available genres or services, a page that shows the movies under the selected category, and a page that shows the movie. The home page has two buttons, allowing users to either search by genre or streaming service. From there, they are taken to a page with all the genres or services. When a user clicks on a movie, they are shown a movie poster and synopsis, along with the genre and streaming service it falls under.

## Backend
-   The backend of our project will need to store a database of movies, the streaming services it is available on, description, genre, and an image.
-   Since a lot of data will need to be stored, we will use Google Firebase as our database. Firebase also allows for authentication features, so it will allow us to populate the database with ease. 
- To test the application, we can use dummy data to check if there are movies displayed when searching for specific genres and streaming services.
- This application will need to access an API to pull data about the movies. We can find an API or database of this movie information and use that data to program our recommendation algorithm.

 # Datasets
Most of the datasets we found didn’t have the pieces of information we wanted.  Just to recap, these are the fields we wanted…
- Movie Name
- Genre
- Overview
- Streaming service
- Image
As mentioned above, there was no one data source that had all of the fields.  So, what we thought of was to find one primary source, and then search through sub-data sources to cross check the fields.

Our main source is the “IMDB Movies Dataset”, which has the fields name, image, genre, and overview.  However, the whole point of the app is to filter by streaming service.  So, we’ll have datasets for each streaming service and populate each movie based on what streaming service it is a part of.

Here is the logic to how we’ll populate our database:
1. Use the IMDB Movies Dataset and populate all the movies with the following fields of movie name, genre, overview, and image
2. Now go through our streaming services data sources.  For each movie on that datasource, find it in the IMDB movies dataset, and populate it
3. Now, the default streaming service is illegal.  So, if a movie has no streaming service, a person needs to resort to mischievous actions.

Data ingest timing is also an important consideration.  However, since this is a one time ingest, timing doesn’t really matter.


## Running the Application:
Created a virtual environment:
- Create the virtual environment in the project folder using python3 -m venv venv 
- Go into virtual environment using source venv/bin/activate 
- Download all the packages needed using pip install -r path/requirements.txt 


Run the application:
- Run the backend using python backend/app.py
- Run the frontend using npm start
