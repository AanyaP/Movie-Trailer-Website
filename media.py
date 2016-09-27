"""

 * Project 1 : Movie Trailer Website
 * Full Stack Web Developer Nanodegree
 * 7/6/2015
 * Instructor - Kunal
 * Author - Aanya

"""

import webbrowser


class Video(object):
        """ This class provides a way to store
            title and duration of movie  """

        # Declaring title and duration
        title = ""
        duration = ""

        # Initializing class Video
        def __init__(self, v_title, v_duration):

                Video.title = v_title
                Video.duration = v_duration

        VALID_RATINGS = ["G", "PG", "PG-13", "R"]


class Movie(Video):
        """ This class provides a way to store
            movie related information  """

        # Initializing class Movie
        def __init__(self, title, movie_ratings,
                     movie_storyline, movie_poster_image,
                     movie_trailer_youtube_url):

            self.title = Video.title
            self.duration = Video.duration
            self.ratings = movie_ratings
            self.storyline = movie_storyline
            self.poster_image_url = movie_poster_image
            self.trailer_youtube_url = movie_trailer_youtube_url

        # Function to show movie trailer
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
