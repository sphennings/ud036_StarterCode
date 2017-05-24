import fresh_tomatoes

# Creates and opens a site containing the posters and trailers of 6 of my
# favorite movies.

# The heavy lifting is done by fresh tomatoes which does the heavy lifting of
# generating html and opening the generated page in a browser. All we need to
# do is pass it a list of movie objects.

# If we're going to pass fresh tomatoes a list of movie objects we will need to
# define a movie object.I'm not sure why fresh tomatoes doesn't define the class
# it consumes I guess it's a homework thing.
class Movie():
    """A quick small class to feed to fresh tomatoes"""
    def __init__(self,
                 movie_title,
                 poster_image,
                 trailer_youtube):
        """The simplest of constructors"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# We need to instantiate the movie objects with titles, posters and trailers.

# A linguist saves the world through language, and also time travel.
the_arrival = media.Movie("The Arival",
                    "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_"
                    "Movie_Poster.jpg",
                    "https://www.youtube.com/watch?v=AMgyWT075KY")

# Giant robots fight giant monsters in the Pacific.
pacific_rim = media.Movie("Pacific Rim",
                    "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim"
                    "_FilmPoster.jpeg",
                    "https://www.youtube.com/watch?v=5guMumPFBag")

# A girl encounters faeries during the Spanish Civil War.
pans_labyrinth = media.Movie("Pans Labyrinth",
                       "https://upload.wikimedia.org/wikipedia/en/6/67/Pan%27s_"
                       "Labyrinth.jpg",
                       "https://www.youtube.com/watch?v=EqYiSlkvRuw")

# Normal people seek shelter in a mad scientist's castle after their
# car broke down.
rocky_horror = media.Movie("Rocky Horror Picture Show",
                     "https://upload.wikimedia.org/wikipedia/en/4/4a/The_Rocky_"
                     "Horror_Picture_Show.jpg",
                     "https://www.youtube.com/watch?v=Pgx1QZFNMz8")

# 120 minutes of chrome high octane awesomeness!
mad_max = media.Movie("Mad Max: Fury Road",
                "http://www.impawards.com/intl/australia/2015/posters/mad_max_"
                "fury_road_ver13_xlg.jpg",
                "https://www.youtube.com/watch?v=hEJnMQG9ev8")

# After being banished from his village a young man must seek
# the god of the forrest.
princess_mononoke = media.Movie("Princess Mononoke",
                          "https://upload.wikimedia.org/wikipedia/en/2/24/"
                          "Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                          "https://www.youtube.com/watch?v=4OiMOHRDs14")


# Make a nice list of all of my favorite movies and hand it off to fresh
# tomatoes to do all the real work.
movies = [the_arrival, pacific_rim, pans_labyrinth,
          rocky_horror, mad_max, princess_mononoke]
fresh_tomatoes.open_movies_page(movies)
