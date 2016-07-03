from unittest import main, TestCase
from models import Character, Teams
from setupDB import create_db
import requests

class TestModels(TestCase):

	# ---------
	# character
	# ---------

	def test_character_1(self):
		c = Character.query.filter_by("Bruce Wayne")
		self.assertEqual (c.name, "Bruce Wayne")
		self.assertEqual (c.alias, "Batman")
		self.assertEqual (c.alignment, "Good")
		self.assertEqual (c.creators, 2)
		self.assertEqual (c.affiliation, 6)

	def test_character_2(self):
		c = Character.query.filter_by("Clark Joseph Kent")
		self.assertEqual (c.name, "Clark Joseph Kent")
		self.assertEqual (c.alias, "Superman")
		self.assertEqual (c.alignment, "Good")
		self.assertEqual (c.creators, 2)
		self.assertEqual (c.affiliation, 6)
	
	def test_character_3(self):
		c = Character.query.filter_by("Diana of Themyscira")
		self.assertEqual (c.name, "Diana of Themyscira")
		self.assertEqual (c.alias, "Wonder Woman")
		self.assertEqual (c.alignment, "Good")
		self.assertEqual (c.creators, 1)
		self.assertEqual (c.affiliation, 2)

	def test_character_repr_1(self):
        actual = str(Character.query.filter_by("Bruce Wayne"))
        self.assertEqual(actual, "<name Bruce Wayne>")

	def test_character_repr_2(self):
        actual = str(Character.query.filter_by("Clark Joseph Kent"))
        self.assertEqual(actual, "<name Clark Joseph Kent>")
	
	def test_character_repr_1(self):
        actual = str(Character.query.filter_by("Diana of Themyscira"))
        self.assertEqual(actual, "<name Diana of Themyscira>")

    # ---------
	# teams
	# ---------
	
	def test_team_1(self):
		team = Team.query.filter_by("Justice League of America")
		self.assertEqual (team.name, "Justice League of America")
		self.assertEqual (team.members, 7)
		self.assertEqual (team.alignment, 16)
		self.assertEqual (team.first_appearance, "Brave and the Bold #28")
		self.assertEqual (team.base_of_operations, "Justice League Headquarters")

	def test_team_2(self):
		c = Team.query.filter_by("The Injustice League")
		self.assertEqual (team.name, "The Injustice League")
		self.assertEqual (team.members, 50)
		self.assertEqual (team.allies, 0)
		self.assertEqual (team.first_appearance, "Justice League of American Wedding Special (Volume 2) #1")
		self.assertEqual (team.base_of_operations, "Hall of Doom")
	
	def test_team_3(self):
		c = Team.query.filter_by("Green Lantern Corps")
		self.assertEqual (team.name, "Green Lantern Corps")
		self.assertEqual (team.members, 31)
		self.assertEqual (team.allies, 0)
		self.assertEqual (team.first_appearance, "Showcase #22")
		self.assertEqual (team.base_of_operations, "Oa")


	def test_character_repr_1(self):
        actual = str(Team.query.filter_by("Justice League of America"))
        self.assertEqual(actual, "<name Justice League of America>")

	def test_character_repr_2(self):
        actual = str(Team.query.filter_by("The Injustice League"))
        self.assertEqual(actual, "<name The Injustice League>")
	
	def test_character_repr_3(self):
        actual = str(Team.query.filter_by("Green Lantern Corps"))
        self.assertEqual(actual, "<name Green Lantern Corps>")

    # ---------
	# Comics
	# ---------

	def test_comics_1(self):
		c = Comic.query.filter_by("Brave and the Bold Vol 1")
		self.assertEqual (c.name, "Brave and the Bold Vol 1")
		self.assertEqual (c.issue, "#28")
		self.assertEqual (c.date, "March, 1960")
		self.assertEqual (c.writer, "Gardner Fox")
		self.assertEqual (c.featured_characters, "Batman")

	def test_comics_2(self):
		c = Comic.query.filter_by("Showcase Vol 1")
		self.assertEqual (c.name, "Showcase Vol 1")
		self.assertEqual (c.issue, "#4")
		self.assertEqual (c.date, "October, 1956")
		self.assertEqual (c.writer, "Robert Kanigher")
		self.assertEqual (c.featured_characters, "Green Lantern")

	def test_comics_3(self):
		c = Comic.query.filter_by("Superman Vol 1")
		self.assertEqual (c.name, "Superman Vol 1")
		self.assertEqual (c.issue, "#76")
		self.assertEqual (c.date, "June, 1952")
		self.assertEqual (c.writer, "Edmond Hamilton")
		self.assertEqual (c.featured_characters, "Superman")

	def test_comics_repr_1(self):
        actual = str(Comic.query.filter_by("Brave and the Bold Vol 1"))
        self.assertEqual(actual, "<name Brave and the Bold Vol 1>")

	def test_comics_repr_2(self):
        actual = str(Comic.query.filter_by("Showcase Vol 1"))
        self.assertEqual(actual, "<name Showcase Vol 1>")
	
	def test_comics_repr_3(self):
        actual = str(Comic.query.filter_by("Superman Vol 1"))
        self.assertEqual(actual, "<name Superman Vol 1>")

	# ---------
	# Movies
	# ---------

	def test_movies_1(self):
		c = Movie.query.filter_by("Watchmen")
		self.assertEqual (c.name, "Watchmen")
		self.assertEqual (c.director, "Zack Snyder")
		self.assertEqual (c.date, "March 6, 2009")
		self.assertEqual (c.featured_characters, 5)
		self.assertEqual (c.distributors, "Warner Bros.")
		self.assertEqual (c.composers, "Tyler Bates")

	def test_movies_2(self):
		c = Movie.query.filter_by("Batman v Superman: Dawn of Justice")
		self.assertEqual (c.name, "Batman v Superman: Dawn of Justice")
		self.assertEqual (c.director, "Zack Snyder")
		self.assertEqual (c.date, "March 25, 2016")
		self.assertEqual (c.featured_characters, 2)
		self.assertEqual (c.distributors, "Warner Bros.")
		self.assertEqual (c.composers, "Hans Zimmer")

	def test_movies_3(self):
		c = Movie.query.filter_by("Justice League: The Flashpoint Paradox")
		self.assertEqual (c.name, "Justice League: The Flashpoint Paradox")
		self.assertEqual (c.director, "James Tucker")
		self.assertEqual (c.date, "July 30, 2013")
		self.assertEqual (c.featured_characters, 1)
		self.assertEqual (c.distributors, "Warner Bros.")
		self.assertEqual (c.composers, "Frederik Wiedmann")

	def test_movies_repr_1(self):
        actual = str(Movie.query.filter_by("Watchmen"))
        self.assertEqual(actual, "<name Watchmen>")

	def test_movies_repr_2(self):
        actual = str(Movie.query.filter_by("Batman v Superman: Dawn of Justice"))
        self.assertEqual(actual, "<name Batman v Superman: Dawn of Justice>")
	
	def test_movies_repr_3(self):
        actual = str(Movie.query.filter_by("Justice League: The Flashpoint Paradox"))
        self.assertEqual(actual, "<name Justice League: The Flashpoint Paradox>")

	# ---------
	# Tv Shows
	# ---------

	def test_tv_1(self):
		c = Show.query.filter_by("Batman")
		self.assertEqual (c.name, "Batman")
		self.assertEqual (c.characters, 6)
		self.assertEqual (c.creators, 2)
		self.assertEqual (c.network, "ABC")
		self.assertEqual (c.first_aired, "January 12, 1966")

	def test_tv_2(self):
		c = Show.query.filter_by("Young Justice")
		self.assertEqual (c.name, "Young Justice")
		self.assertEqual (c.characters, 6)
		self.assertEqual (c.creators, 2)
		self.assertEqual (c.network, "Cartoon Network")
		self.assertEqual (c.first_aired, "November 2010")

	def test_tv_3(self):
		c = Show.query.filter_by("The Flash")
		self.assertEqual (c.name, "The Flash")
		self.assertEqual (c.characters, 1)
		self.assertEqual (c.creators, 3)
		self.assertEqual (c.network, "CW")
		self.assertEqual (c.first_aired, "October 7, 2014")

	def test_tv_repr_1(self):
        actual = str(Show.query.filter_by("Batman"))
        self.assertEqual(actual, "<name Batman>")

	def test_tv_repr_2(self):
        actual = str(Show.query.filter_by("Young Justice"))
        self.assertEqual(actual, "<name Young Justice>")
	
	def test_tv_repr_3(self):
        actual = str(Show.query.filter_by("The Flash"))
        self.assertEqual(actual, "<name The Flash>")


	# ---------
	# Creator
	# ---------

	def test_creator_1(self):
		c = Creator.query.filter_by("Bob Kane")
		self.assertEqual (c.name, "Bob Kane")
		self.assertEqual (c.occupation, "Writer")
		self.assertEqual (c.birth_year, "October 24, 1915")
		self.assertEqual (c.birth_place, "New York City, New York, United States of America")
		self.assertEqual (c.creations, 8)
		self.assertEqual (c.first_publication, "New Adventure Comics Vol 1 26")

	def test_creator_2(self):
		c = Creator.query.filter_by("Grant Morrison")
		self.assertEqual (c.name, "Grant Morrison")
		self.assertEqual (c.occupation, "Writer")
		self.assertEqual (c.birth_year, "January 31, 1960")
		self.assertEqual (c.birth_place, "Glasgow Scotland")
		self.assertEqual (c.creations, 1)
		self.assertEqual (c.first_publication, "Animal Man #1")

	def test_creator_3(self):
		c = Creator.query.filter_by("Zack Snyder")
		self.assertEqual (c.name, "Zack Snyder")
		self.assertEqual (c.occupation, "Director")
		self.assertEqual (c.birth_year, "March 1, 1966")
		self.assertEqual (c.birth_place, "Green Bay, Wisconsin, United States of America")
		self.assertEqual (c.creations, 0)
		self.assertEqual (c.first_publication, "Watchmen (Movie)")

	def test_tv_repr_1(self):
        actual = str(Creator.query.filter_by("Bob Kane"))
        self.assertEqual(actual, "<name Bob Kane>")

	def test_tv_repr_2(self):
        actual = str(Creator.query.filter_by("Grant Morrison"))
        self.assertEqual(actual, "<name Grant Morrison>")
	
	def test_tv_repr_3(self):
        actual = str(Creator.query.filter_by("Zack Snyder"))
        self.assertEqual(actual, "<name Zack Snyder>")