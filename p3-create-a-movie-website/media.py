# Intro to Programming Nanodegree
# Project 3 - Create a Movie Website
# Ricardo Yoshitomi

import webbrowser

class Movie(object):
	"""This class provides a way to store movie related information"""
	def __init__(self, movie_title, brief_description, poster_image, trailer_youtube):
		"""initialize instance of class Movie"""
		self.title = movie_title
		self.description = brief_description
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	def show_trailer(self):
		"""open the web browser with the correct url"""
		webbrowser.open(self.trailer_youtube_url)

class Info(Movie):
	"""This class inherits from class Movie and provides aditional informations"""
	def __init__(self, movie_title, brief_description, poster_image, trailer_youtube, directed_by, movie_writers, starring, release_year, movie_genre, running_time, movie_country, movie_language, release_date):
		"""initialize instance of class Info"""
		super(Info, self).__init__(movie_title, brief_description, poster_image, trailer_youtube)
		self.director = directed_by
		self.writers = movie_writers
		self.stars = starring
		self.year = release_year
		self.genre = movie_genre
		self.duration = running_time
		self.country = movie_country
		self.language = movie_language
		self.date=release_date
