import webbrowser

# U413 - 1.1 Identify and structure the components and data
# required to address problems
# You can see a set of classes being created, which are made to
# display TV-series in a list.

# The Parent class is being created
class Show():
    def __init__(self, shtitle, shstory, posterimg, traileryt):
        # the title of movie
        self.title = shtitle
        # the story of the movie
        self.storyline = shstory
        # the image of the movie
        self.poster_image_url = posterimg
        # the trailer of the movie
        self.trailer_youtube_url = traileryt
        show_type = 'Show'
    def type_print(self):
        raise NotImplementedError("Subclass must implement abstract method")


# CW - 1.2 b The two classes below are both inheriting characterisitcs from
# the class Show, the reason for doing that is because the TV-series and the
# Movies both have simiar qualites, e.g. they both have a title or a
# description.
# TV-series Child class being created
class TV_serie(Show):
	def __init__(self, shtitle, shstory, posterimg, traileryt, s_episodes, s_seasons):  # noqa
            Show.__init__(self, shtitle, shstory, posterimg, traileryt)
            # the number of episodes
            self.episodes = s_episodes
            # the number of seasons
            self.seasons = s_seasons
            
            self.type = 'TV series'


# Movie Child class being created
class Movie(Show):
    def __init__(self, shtitle, shstory, posterimg, traileryt, m_duration, m_parts):  # noqa
            Show.__init__(self, shtitle, shstory, posterimg, traileryt)
            # duartion of the movie
            self.duration = m_duration
            # how many parts of the movie exists
            self.parts = m_parts

            self.type = 'Movie'
