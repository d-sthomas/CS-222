import unittest
import json

import movie_queries
import ingest_data_script

class testFirebaseQueries(unittest.TestCase):
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    def test_get_movie(self):
        # first we are going to upload the data
        imdb = "data_sets/test_imdb_top_1000.csv"
        netflix = ""
        amazon = ""
        hulu = "data_sets/test_hulu_imdb.csv"
        disney = ""
        data = ingest_data_script.build_db(imdb, netflix, amazon, hulu, disney)
        ingest_data_script.upload_firebase(data)

        # now we do our checks
        # 1. check if we can retrieve a movie by title
        output1 = movie_queries.get_movie("Anushka")
        # print(output1)
        assert output1["Series_Title"] == "Anushka"
        
        # 2. check if we can get these movies by genre
        output2 = movie_queries.get_movie_by_genre("testGenre")
        # print(output2)
        for dat in output2:
            assert "testGenre" in dat["Genre"]
        
        # 3. check if we can get these movies by streaming service
        output3 = movie_queries.get_movie_by_streaming_service("Hulu")
        # data3 = json.load(output3)
        for dat in output3:
            assert "Hulu" in dat["streaming"]
        
        
if __name__ == '__main__':
    unittest.main()