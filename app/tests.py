from unittest import main, TestCase
from models import *
import requests


class TestModels(TestCase):
    
    # ---------
    # character
    # ---------

    def test_character_1(self):
        c = Characters.query.filter_by(title = "Batman (Bruce Wayne)").first()
        self.assertEqual(c.real_name, "Bruce Wayne")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.alignment, "Good")
        self.assertEqual(c.debut, "1986")
        self.assertEqual(c.identity, "Secret Identity")
        self.assertEqual(c.creators, ["Bob Kane", "Bill Finger"])
        self.assertEqual(c.universes, ["New Earth"])
        self.assertEqual(c.aliases, ["Batman", "Insider", "Matches Malone", "Robin"])
        self.assertEqual(c.affiliation,  ['Batman Family', 'Justice League' , 'Batman Incorporated', 'Outsiders','Wayne Enterprises', \
            'Club of Heroes', 'formerly White Lantern Corps', 'Sinestro Corps'])

    def test_character_2(self):
        c = Characters.query.filter_by(title = "Flash (Barry Allen)").first()
        self.assertEqual(c.real_name, "Bartholomew Henry \"Barry\" Allen")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.alignment, "Good")
        self.assertEqual(c.debut, "1956")
        self.assertEqual(c.identity, "Secret Identity")
        self.assertEqual(c.creators, ["Carmine Infantino", "Robert Kanigher"])
        self.assertEqual(c.universes, ["Earth-One", "New Earth" ] )
        self.assertEqual(c.aliases, ["The Flash", "Black Flash", "Parallax"])
        self.assertEqual(c.affiliation, ['Justice League', 'Flash Family', 'formerly Blue Lantern Corps', 'White Lantern Corps'])

    def test_character_3(self):
        c = Characters.query.filter_by(title = "Joker (Earth 3)").first()
        self.assertEqual(c.real_name, "Unknown")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.alignment, "Good")
        self.assertEqual(c.debut, "2013")
        self.assertEqual(c.identity, "Secret Identity")
        self.assertEqual(c.creators, ["Ivan Reis", "Geoff Johns"])
        self.assertEqual(c.universes, ["Earth 3"] )
        self.assertEqual(c.aliases, ["The Joker"])
        self.assertEqual(c.affiliation, "Not available")

    # # ---------
    # # teams
    # # ---------

    def test_team_1(self):
        team = Teams.query.filter_by(title = "The Elite (Prime Earth)").first()
        self.assertEqual(team.title, "The Elite (Prime Earth)")
        self.assertEqual(team.team_leaders, ['Manchester Black', 'Wonder Girl'])
        self.assertEqual(team.universes, ['Prime Earth'])
        self.assertEqual(team.identity, "Secret")
        self.assertEqual(team.status, "Active")

    def test_team_2(self):
        team = Teams.query.filter_by(title = "Justice League (Earth-16)").first()
        self.assertEqual(team.title, "Justice League (Earth-16)")
        self.assertEqual(team.team_leaders, ['Black Canary', 'Captain Atom', 'Batman (formerly)'])
        self.assertEqual(team.universes, ['Earth-16'])
        self.assertEqual(team.identity, "Public")
        self.assertEqual(team.status, "Active")

    def test_team_3(self):
        team = Teams.query.filter_by(title = "Seven Men of Death").first()
        self.assertEqual(team.title, "Seven Men of Death")
        self.assertEqual(team.team_leaders, ['Talia Head', 'formerly Sensei'])
        self.assertEqual(team.universes, ['New Earth', 'Prime Earth'])
        self.assertEqual(team.identity, "Secret")
        self.assertEqual(team.status, "Active")

    # ---------
    # Comics
    # ---------

    def test_comics_1(self):
        c = Comics.query.filter_by(title = "Batman: Arkham Knight Annual Vol 1 1").first()
        self.assertEqual(c.title, "Batman: Arkham Knight Annual Vol 1 1")
        self.assertEqual(c.locations, ['Gotham_City', 'Gotham_City_Chinatown', 'Wayne_Manor'])
        self.assertEqual(c.release_date, "{November,2015}")
        self.assertEqual(c.featured_characters, ['Jason_Todd_(Arkhamverse)'])
        self.assertEqual(c.creators, ['Brittany Holzherr', 'Andy Kubert', 'Peter Tomasi', 'Stephen Segovia', 'Art Thibert', 'Kelsey Shannon', 'Deron Bennett'])

    def test_comics_2(self):
        c = Comics.query.filter_by(title = "Hal Jordan and the Green Lantern Corps: Rebirth Vol 1 1").first()
        self.assertEqual(c.title, "Hal Jordan and the Green Lantern Corps: Rebirth Vol 1 1")
        self.assertEqual(c.locations, [])
        self.assertEqual(c.release_date, "{September,2016}")
        self.assertEqual(c.featured_characters, [])
        self.assertEqual(c.creators, ['Andrew Marino', 'Ethan Van Sciver', 'Robert Venditti', 'Jason Wright', 'Dave Sharpe'])

    def test_comics_3(self):
        c = Comics.query.filter_by(title = "Justice League Vol 2 31").first()
        self.assertEqual(c.title, "Justice League Vol 2 31")
        self.assertEqual(c.locations, ['Metropolis', 'Gotham_City', 'Wayne_Manor', 'Oregon', 'Portland', '_Oregon'])
        self.assertEqual(c.release_date, "{August,2014}")
        self.assertEqual(c.featured_characters, ['Justice_League_(Prime_Earth)', 'Bruce_Wayne_(Prime_Earth)', 'Victor_Stone_(Prime_Earth)', 'Diana_of_Themyscira_(Prime_Earth)', 'Kal-El_(Prime_Earth)', 'William_Batson_(Prime_Earth)'])
        self.assertEqual(c.creators, ['Brian Cunningham', 'Ivan Reis', 'Geoff Johns', 'Doug Mahnke', 'Keith Champagne', 'Rod Reis', 'Dezi Sienty'])

    # # ---------
    # # Movies
    # # ---------

    def test_movies_1(self):
        c = Movies.query.filter_by(title = "Watchmen (Movie)").first()
        self.assertEqual(c.title, "Watchmen (Movie)")
        self.assertEqual(c.creators, ['William Hoy', 'Zack Snyder', 'David Hayter', 'Alex Tse', 'Roberto Orci', 'Alex Kurtzman', 'Cinematographers', 'Larry Fong'])
        self.assertEqual(c.release_date, "March 6 2009")
        self.assertEqual(c.budget, "$120 million")
        self.assertEqual(c.featured_characters, ['Crimebusters_(Watchmen)', 'Edward_Blake_(Watchmen)', 'Jonathan_Osterman_(Watchmen)', 'Daniel_Dreiberg_(Watchmen)', 'Walter_Kovacs_(Watchmen)', 'Laurel_Juspeczyk_(Watchmen)'])

    def test_movies_2(self):
        c = Movies.query.filter_by(title = "The Batman vs. Dracula (Movie)").first()
        self.assertEqual(c.title, "The Batman vs. Dracula (Movie)")
        self.assertEqual(c.creators, ['Duane Capizzi', 'Michael Goguen'])
        self.assertEqual(c.release_date, "October 18 2005")
        self.assertEqual(c.budget, "Not available")
        self.assertEqual(c.featured_characters, ['Bruce_Wayne_(The_Batman)'])

    def test_movies_3(self):
        c = Movies.query.filter_by(title = "Justice League: Starcrossed (Movie)").first()
        self.assertEqual(c.title, "Justice League: Starcrossed (Movie)")
        self.assertEqual(c.creators, ['Dwayne McDuffie', 'Butch Lukic', 'Dan Riba', 'Rich Fogel'])
        self.assertEqual(c.release_date, "July 13 2004")
        self.assertEqual(c.budget, "Not available")
        self.assertEqual(c.featured_characters, ['Justice_League_(DCAU)', 'Bruce_Wayne_(DCAU)', 'Wallace_West_(DCAU)', 'John_Stewart_(DCAU)', 'Shayera_Hol_(DCAU)', 'J%27onn_J%27onzz_(DCAU)', 'Kal-El_(DCAU)', 'Diana_of_Themyscira_(DCAU)'])

    # ---------
    # Tv Shows
    # ---------

    def test_tv_1(self):
        c = Shows.query.filter_by(title = "Justice League Unlimited (TV Series)").first()
        self.assertEqual(c.creators, ['Bruce Timm', 'James Tucker', 'Dwayne McDuffie'])
        self.assertEqual(c.featured_characters, ['Superman', 'Batman', 'Flash (Wally West', 'Green Lantern (John Stewart)', 'Hawkgirl', "J'onn J'onzz"])
        self.assertEqual(c.first_air_date, "July 31 2004")
        self.assertEqual(c.last_air_date, "May 13 2006")
        self.assertEqual(c.running_time, "Not available") 
        self.assertEqual(c.title, "Justice League Unlimited (TV Series)")       


    def test_tv_2(self):
        c = Shows.query.filter_by(title = "Young Justice (TV Series)").first()
        self.assertEqual(c.creators, ['Greg Weisman', 'Brandon Vietti', 'Sam Register'])
        self.assertEqual(c.featured_characters, ['Artemis', 'Aqualad', 'Kid Flash', 'Miss Martian', 'Robin', 'Super Boy'])
        self.assertEqual(c.first_air_date, "November 2010")
        self.assertEqual(c.last_air_date, "Not available")
        self.assertEqual(c.running_time, "Not available") 
        self.assertEqual(c.title, "Young Justice (TV Series)")  

    def test_tv_3(self):
        c = Shows.query.filter_by(title = "The Flash (2014 TV Series)").first()
        self.assertEqual(c.creators,['Greg Berlanti'])
        self.assertEqual(c.featured_characters, ['Flash'])
        self.assertEqual(c.first_air_date, "October 7th 2014")
        self.assertEqual(c.last_air_date, "Not available")
        self.assertEqual(c.running_time, "Not available") 
        self.assertEqual(c.title, "The Flash (2014 TV Series)")     
    # ---------
    # Creator
    # ---------
    def test_creator_1(self):
        c = Creators.query.filter_by(title = "Grant Morrison").first()
        self.assertEqual(c.birth_date, "January 31 1960")
        self.assertEqual(c.employers, ['DC Comics', 'Vertigo'])
        self.assertEqual(c.first_publication, "Animal Man #1")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.job_titles, ['Writer'])
        self.assertEqual(c.title, "Grant Morrison")
    
    def test_creator_2(self):
        c = Creators.query.filter_by(title = "Scott Snyder").first()
        self.assertEqual(c.birth_date, "January 1 1976")
        self.assertEqual(c.employers, ['DC Comics', 'Vertigo'])
        self.assertEqual(c.first_publication, "Unknown")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.job_titles, ['Writer'])
        self.assertEqual(c.title, "Scott Snyder")



    def test_creator_3(self):
        c = Creators.query.filter_by(title = "William Moulton Marston").first()
        self.assertEqual(c.birth_date, "May 9th 1893")
        self.assertEqual(c.employers, ['DC Comics'])
        self.assertEqual(c.first_publication, "All-Star Comics #8")
        self.assertEqual(c.gender, "Male")
        self.assertEqual(c.job_titles, ['Writer'])
        self.assertEqual(c.title, "William Moulton Marston")

if __name__ == "__main__":
    main()