from unittest import main, TestCase
from models import *
import requests
import sqlite3

class TestModels(TestCase):
	
	# ---------
	# character
	# ---------

	def test_character_1(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Characters (title,gender,real_name, al ,debut, identity) VALUES ('Batman (Bruce Wayne)','Bruce Wayne','Male','Good','1986','Secret Identity' )")
		capt  = conn.execute("SELECT * from Characters")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Batman (Bruce Wayne)')
		self.assertEqual(co[1], "Bruce Wayne")
		self.assertEqual(co[2], "Male")
		self.assertEqual(co[3], "Good")
		self.assertEqual(co[4], "1986")
		self.assertEqual(co[5], "Secret Identity")
		conn.execute('DELETE from Characters')
		conn.commit()
		conn.close()
	def test_character_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Characters (title,gender,real_name, al ,debut, identity) VALUES ('Joker (New Earth)','Unknown','Male','Bad','1985','Secret Identity' )")
		capt  = conn.execute("SELECT * from Characters")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Joker (New Earth)')
		self.assertEqual(co[1], "Unknown")
		self.assertEqual(co[2], "Male")
		self.assertEqual(co[3], "Bad")
		self.assertEqual(co[4], "1985")
		self.assertEqual(co[5], "Secret Identity")
		conn.execute('DELETE from Characters')
		conn.commit()
		conn.close()
	def test_character_3(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Characters (title,gender,real_name, al ,debut, identity) VALUES ('Superman (New Earth)','Clark Kent','Male','Good','1985','Secret Identity' )")
		capt  = conn.execute("SELECT * from Characters")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Superman (New Earth)')
		self.assertEqual(co[1], "Clark Kent")
		self.assertEqual(co[2], "Male")
		self.assertEqual(co[3], "Good")
		self.assertEqual(co[4], "1985")
		self.assertEqual(co[5], "Secret Identity")
		conn.execute("DELETE from Characters")
		conn.commit()
		conn.close()
	# # ---------
	# # teams
	# # ---------
  


	def test_team_1(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Teams (title,identity,status) VALUES ('The Elite (Prime Earth)','Secret','Active')")
		capt  = conn.execute("SELECT * from Teams")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'The Elite (Prime Earth)')
		self.assertEqual(co[1], "Secret")
		self.assertEqual(co[2], "Active")
		conn.execute("DELETE from Teams")
		conn.commit()
		conn.close()

	def test_team_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Teams (title,identity,status) VALUES ('Justice League (Earth-16)','Secret','Active')")
		capt  = conn.execute("SELECT * from Teams")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Justice League (Earth-16)')
		self.assertEqual(co[1], "Secret")
		self.assertEqual(co[2], "Active")
		conn.execute("DELETE from Teams")
		conn.commit()
		conn.close()

	def test_team_3(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Teams (title,identity,status) VALUES ('Seven Men of Death','Secret','Active')")
		capt  = conn.execute("SELECT * from Teams")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Seven Men of Death')
		self.assertEqual(co[1], "Secret")
		self.assertEqual(co[2], "Active")
		conn.execute("DELETE from Teams")
		conn.commit()
		conn.close()

	# ---------
	# Comics
	# ---------
 
	def test_comics_1(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Comics (title,release_date) VALUES ('Batman: Arkham Knight Annual Vol 1 1','{November,2015}' )")
		capt  = conn.execute("SELECT * from Comics")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Batman: Arkham Knight Annual Vol 1 1')
		self.assertEqual(co[1], "{November,2015}")
		conn.execute("DELETE from Comics")
		conn.commit()
		conn.close()
	def test_comics_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Comics (title,release_date) VALUES ('Hal Jordan and the Green Lantern Corps: Rebirth Vol 1 1','{September,2016}' )")
		capt  = conn.execute("SELECT * from Comics")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Hal Jordan and the Green Lantern Corps: Rebirth Vol 1 1')
		self.assertEqual(co[1], "{September,2016}")
		conn.execute("DELETE from Comics")
		conn.commit()
		conn.close()
	def test_comics_3(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Comics (title,release_date) VALUES ('Justice League Vol 2 31','{August,2014}' )")
		capt  = conn.execute("SELECT * from Comics")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Justice League Vol 2 31')
		self.assertEqual(co[1], "{August,2014}")
		conn.execute("DELETE from Comics")
		conn.commit()
		conn.close()
	# # ---------
	# # Movies
	# # ---------




	def test_movies_1(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Movies (title,release_date,budget) VALUES ( 'Watchmen (Movie)','March 6 2009', '120 million' )")
		capt  = conn.execute("SELECT * from Movies")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Watchmen (Movie)')
		self.assertEqual(co[1], "March 6 2009")
		self.assertEqual(co[2], "120 million")
		conn.execute("DELETE from Movies")
		conn.commit()
		conn.close()
	def test_movies_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Movies (title,release_date,budget) VALUES ( 'The Batman vs. Dracula (Movie)','October 18 2005', 'Not available' )")
		capt  = conn.execute("SELECT * from Movies")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'The Batman vs. Dracula (Movie)')
		self.assertEqual(co[1], "October 18 2005")
		self.assertEqual(co[2], "Not available")
		conn.execute("DELETE from Movies")
		conn.commit()
		conn.close()

	def test_movies_3(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Movies (title,release_date,budget) VALUES ( 'Justice League: Starcrossed (Movie)','July 13 2004', 'Not available' )")
		capt  = conn.execute("SELECT * from Movies")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Justice League: Starcrossed (Movie)')
		self.assertEqual(co[1], "July 13 2004")
		self.assertEqual(co[2], "Not available")
		conn.execute("DELETE from Movies")
		conn.commit()
		conn.close()
	# ---------
	# Tv Shows
	# ---------


	def test_tv_1(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Shows (title,first_air_date,last_air_date) VALUES ( 'Justice League Unlimited (TV Series)','July 31 2004', 'May 13 2006')")
		capt  = conn.execute("SELECT * from Shows")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Justice League Unlimited (TV Series)')
		self.assertEqual(co[1], "July 31 2004")
		self.assertEqual(co[2], "May 13 2006")
		conn.execute("DELETE from Shows")
		conn.commit()
		conn.close()

	def test_tv_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Shows (title,first_air_date,last_air_date) VALUES ( 'Young Justice (TV Series)','November 2010', 'Not available' )")
		capt  = conn.execute("SELECT * from Shows")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Young Justice (TV Series)')
		self.assertEqual(co[1], "November 2010")
		self.assertEqual(co[2], "Not available")
		conn.execute("DELETE from Shows")
		conn.commit()
		conn.close()

	def test_tv_3(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Shows (title,first_air_date,last_air_date) VALUES ( 'The Flash (2014 TV Series)','October 7th 2014', 'Not available' )")
		capt  = conn.execute("SELECT * from Shows")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'The Flash (2014 TV Series)')
		self.assertEqual(co[1], "October 7th 2014")
		self.assertEqual(co[2], "Not available")
		conn.execute("DELETE from Shows")
		conn.commit()
		conn.close() 
	# ---------
	# Creator
	# ---------

   
	def test_creator_1(self):

		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Creators (title,birth_date,first_publication) VALUES ( 'Grant Morrison','January 31 1960','Animal Man #1')")
		capt  = conn.execute("SELECT * from Creators")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Grant Morrison')
		self.assertEqual(co[1], "January 31 1960")
		self.assertEqual(co[2], "Animal Man #1")
		conn.execute("DELETE from Creators")
		conn.commit()
		conn.close() 
	
	def test_creator_2(self):
		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Creators (title,birth_date,first_publication) VALUES ( 'Scott Snyder','January 1 1976','Unknown' )")
		capt  = conn.execute("SELECT * from Creators")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'Scott Snyder')
		self.assertEqual(co[1], "January 1 1976")
		self.assertEqual(co[2], "Unknown")
		conn.execute("DELETE from Creators")
		conn.commit()
		conn.close() 
	def test_creator_3(self):

		conn = sqlite3.connect('test.db')
		conn.execute("INSERT INTO Creators (title,birth_date,first_publication) VALUES ( 'William Moulton Marston','May 9th 1893','All-Star Comics #8' )")
		capt  = conn.execute("SELECT * from Creators")
		co = capt.fetchone() 
		self.assertEqual(co[0], 'William Moulton Marston')
		self.assertEqual(co[1], "May 9th 1893")
		self.assertEqual(co[2], "All-Star Comics #8")
		conn.execute("DELETE from Creators")
		conn.commit()
		conn.close() 

if __name__ == "__main__":
	conn = sqlite3.connect('test.db')
	conn.execute("DROP TABLE IF EXISTS Creators")
	conn.execute("DROP TABLE IF EXISTS Teams")
	conn.execute("DROP TABLE IF EXISTS Comics")
	conn.execute("DROP TABLE IF EXISTS Movies")
	conn.execute("DROP TABLE IF EXISTS Shows")
	conn.execute("DROP TABLE IF EXISTS Characters")

	conn.execute('''CREATE TABLE Creators
	   (title 		  Text  PRIMARY KEY     NOT NULL,
	   birth_date         TEXT   ,
	   first_publication, 		Text  )''')
	conn.execute('''CREATE TABLE Teams
	   (title 		  Text  PRIMARY KEY     NOT NULL,
	   identity           TEXT   ,
	   status           Text )''')
	conn.execute('''CREATE TABLE Comics
	   (title 		  Text  PRIMARY KEY     NOT NULL,
	   release_date           TEXT  )''')
	conn.execute('''CREATE TABLE Movies
	   (title 		  Text  PRIMARY KEY     NOT NULL,
	   release_date           TEXT   ,
	   budget  		Text )''')
	conn.execute('''CREATE TABLE Shows
	   (title 		  Text  PRIMARY KEY     NOT NULL,
	   first_air_date           TEXT ,
	   last_air_date, 		Text )''')
	conn.execute('''CREATE TABLE Characters
             (title text, gender text, real_name text, al text, debut text, identity text)''')
	conn.commit()
	conn.close()
	main()
