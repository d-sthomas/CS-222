import unittest

from ingestDataScript import ingestMoviesFromCSV

# logic for this class:
    # for each data source, these are the followign checks
        # checks the length
        # checks for contents

class ingestDataScript(unittest.TestCase):
    # test imdb data 
    # this tests if the size of the data that is returned is correct
    def testIMDBDataSize():
        dataRetrieved = ingestMoviesFromCSV('test_imdb_titles.csv', "") # small data file
        self.assertEqual(len(dataRetrieved), 3, "the length of the data should be 3")
    # this tests if the contents are the same
    def testIMDBDataContents():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV('test_imdb_titles.csv',"") # small data file
        self.assertEqual(dataRetrieved[0], {'name': 'From Here to Eternity', 'image': 'https://m.media-amazon.com/images/M/MV5BM2U3YzkxNGMtYWE0YS00ODk0LTk1ZGEtNjk3ZTE0MTk4MzJjXkEyXkFqcGdeQXVyNDk0MDg4NDk@._V1_UX67_CR0,0,67,98_AL_.jpg'})
        self.assertEqual(dataRetrieved[1], {'name': 'Lifeboat', 'image': 'https://m.media-amazon.com/images/M/MV5BZTBmMjUyMjItYTM4ZS00MjAwLWEyOGYtYjMyZTUxN2I3OTMxXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX67_CR0,0,67,98_AL_.jpg'})
        self.assertEqual(dataRetrieved[2], {'name': 'The 39 Steps', 'image': 'https://m.media-amazon.com/images/M/MV5BMTY5ODAzMTcwOF5BMl5BanBnXkFtZTcwMzYxNDYyNA@@._V1_UX67_CR0,0,67,98_AL_.jpg'})

    # test amazon data 
    # this tests if the size of the data that is returned is correct
    def testAmazonPrimeDataSize():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_amazon_prime_titles.csv", "amazonPrime") # small data file
        self.assertEqual(len(dataRetrieved), 4, "the length of the data should be 4")
    # this tests if the contents are the same
    def testAmazonPrimeDataContents():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_amazon_prime_titles.csv", "amazonPrime") # small data file
        self.assertEqual(dataRetrieved[0], {'year': '2008', 'name': 'Outpost', 'plot': 'In war-torn Eastern Europe, a world-weary group of mercenaries discover a long-hidden secret in an abandoned WWII bunker.', 'rating': 'R', 'streamingService': 'amazonPrime'})
        self.assertEqual(dataRetrieved[1], {'year': '2010', 'name': 'Harry Brown', 'plot': "Harry Brown, starring two-time Academy Award winner Michael Caine, follows one man's journey through a chaotic world where teenage violence runs rampant. As a modest, law abiding citizen, Brown lives alone. His only companion is his best friend Leonard. When Leonard is killed, Brown reaches his breaking point. Harry Brown is a powerful, character driven thriller.", 'rating': 'R', 'streamingService': 'amazonPrime'})

    # test disney plus data 
    # this tests if the size of the data that is returned is correct
    def testDisneyPlusDataSize():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_disney_plus_shows.csv", "disneyPlus") # small data file
        self.assertEqual(len(dataRetrieved), 2, "the length of the data should be 2")
    # this tests if the contents are the same
    def testDisneyPlusDataContents():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_disney_plus_shows.csv", "disneyPlus") # small data file
        self.assertEqual(dataRetrieved[0], {'year': '2018', 'name': 'Z-O-M-B-I-E-S', 'genre': 'FAMILY, MUSICAL, ROMANCE', 'plot': 'Students from Zombietown are transferred to a high school in a suburban town preoccupied with uniformity, traditions and pep rallies.', 'rating': '6.3', 'streamingService': 'disneyPlus'})
        self.assertEqual(dataRetrieved[1], {'year': '2014', 'name': 'Zapped', 'genre': 'COMEDY, FAMILY, FANTASY', 'plot': "When Zoey's mom remarries, Zoey finds it hard adjusting to her new life - no longer the only kid in the family.", 'rating': '5.1', 'streamingService': 'disneyPlus'})

    # test hulu data 
    # this tests if the size of the data that is returned is correct
    def testHuluDataSize():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_hulu_titles.csv", "hulu") # small data file
        self.assertEqual(len(dataRetrieved), 1, "the length of the data should be 1")
     # this tests if the contents are the same
    def testHuluDataContents():
        # number of entries, content and these are two different functions
        dataRetrieved = ingestMoviesFromCSV("test_hulu_titles.csv", "hulu") # small data file
        self.assertEqual(dataRetrieved[0], {'year': '2021', 'name': "Ricky Velez: Here's Everything", 'plot': 'Comedian Ricky Velez bares it all with his honest lens and down to earth perspective in his first-ever HBO stand-up special.', 'rating': 'TV-MA', 'streamingService': 'hulu'})




# create dummyMovie to DB and use direct firebase call clean up by deleting movie
# get dummyMovie by calling the function
