import webbrowser

#class movie here to store movies, bio, pics ect.
class Movie():

#def__init__ is the constructor Movie and has four instance variables.
    def __init__(self, movie_title, movie_bio, poster_image, trailer_youtube):
        self.title = movie_title
        self.bio = movie_bio
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#def show trailer here as a instance method to play the trailer video.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
