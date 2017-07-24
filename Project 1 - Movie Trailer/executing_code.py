# comiplersite is the piece of code that contains function, which compiles all
# of my instances.
import compilersite
# media is a class file which contains all of the class variables
import media

# ~~~~~~~~~~ MOVIES ~~~~~~~~~~

# Iron man instance
iron_man = media.Movie(
    'Iron man 3',
    "Marvel's 'Iron Man 3' pits brash-but-brilliant industrialist Tony Stark"
    "/Iron Man against an enemy whose reach knows no bounds. When Stark f"
    "inds his personal world destroyed at his enemy's hands, he embarks on"
    " a harrowing quest to find those responsible. This journey, at every "
    "turn, will test his mettle.",
    'https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg',  # noqa
    'https://www.youtube.com/watch?v=Ke1Y3P9D0Bc', '130min', '3')

# Southpaw instance
southpaw = media.Movie(
    'Southpaw',
    'Boxer Billy Hope turns to trainer Tick Wills to help him get his life bac'
    'k on track after losing his wife in a tragic accident and his daughte'
    'r to child protection services.',
    'http://ia.media-imdb.com/images/M/MV5BMjI1MTcwODk0MV5BMl5BanBnXkFtZTgwMTgwMDM5NTE@._V1_SX640_SY720_.jpg',  # noqa
    'https://www.youtube.com/watch?v=Mh2ebPxhoLs', '124min', '1')

# Warrior instance
warrior = media.Movie(
    'Warrior', 'The youngest son of an alcoholic former boxer returns home, where he is trained by his father'
    ' for competition in a mixed martial arts tournament a path that puts the fighter on a collision corner'
    'with his older brother.',
    'http://www.gstatic.com/tv/thumb/movieposters/8063104/p8063104_p_v8_az.jpg',  # noqa
    'https://www.youtube.com/watch?v=kY7HcUACs58', '140min', '1')

# ~~~~~~~~~~ TV SERIES ~~~~~~~~~~

# Game of thrones instance
game_of_thrones = media.TV_serie(
    'Game of Thrones',
    'While a civil war brews between several noble families in Westeros, the '
    'children of the former rulers of the land attempt to rise up to power'
    '. Meanwhile a forgotten race, bent on destruction, return after.'
    'thousands of years in the North.',
    'http://www.gstatic.com/tv/thumb/tvbanners/11418130/p11418130_b_v8_aa.jpg',
    'https://www.youtube.com/watch?v=OmrA8nOZF2Q', '10', '6')

# Vikings instance
vikings = media.TV_serie(
    'Vikings',
    'The world of the Vikings is brought to '
    'life through the journey of Ragnar Lothbrok, the first Viking to '
    'emerge from Norse legend and onto the pages of history - a man on'
    ' the edge of myth.',
    'http://www.gstatic.com/tv/thumb/tvbanners/12452768/p12452768_b_v8_aa.jpg',
    'https://www.youtube.com/watch?v=xdm7Z3TQhDg', '9-10', '4')

# TV-series array
tv_series = [game_of_thrones, vikings]

# Movies array
movies = [iron_man, southpaw, warrior]

# Shows array
shows = [southpaw, game_of_thrones, iron_man, vikings, warrior]

#Test for classes functionality + evidence CW 1.2 - Polymorphism
for show in shows:
    print str(show.title) + ': ' + show.type

# The line below call the function in the "compilersite.py" file and runs the
# movies array and the tv_series array
compilersite.open_movies_page(movies, tv_series)

