from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/dcdatabase'
db = SQLAlchemy(app)


class Character(db.Model):

    """
    DC characters with attributes title, hero/villain alias, an image,
    their alignment, and other information
    """

    __tablename__ = 'characters'

    id = db.Column(db.Integer)
    title = db.Column(db.String(50), primary_key=True)
    creators = db.Column(ARRAY(db.String(100)))
    alignment = db.Column(db.String(50))
    identity = db.Column(db.String(50))
    real_name = db.Column(db.String(50))
    universe = db.Column(ARRAY(db.String(100)))
    image = db.Column(db.String(250))
    status = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    debut = db.Column(db.String(50))
    aliases = db.Column(ARRAY(db.String(100)))

    def __init__(self, title, alias, image, alignment, creators, identity, real_name, universe, status, gender, debut, aliases):
        """
        Initialize the character
        """
        self.title = title
        self.aliases = aliases
        self.image = image
        self.alignment = alignment
        self.creators = creators
        self.identity = identity
        self.real_name = real_name
        self.universe = universe
        self.status = status
        self.gender = gender
        self.debut = debut

    def __repr__(self):
        """
        Return represenation of this character in format
        <alias {}> where {} is character's alias

        So the Character Bruce Wayne is represented as Batman
        """
        return '<alias {}>'.format(self.alias)

    def to_json(self, list_view = False):
        """
        Return a dictionary of information of this character
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'creators' : self.creators,
            'alignment' : self.alignment,
            'identity' : self.identity,
            'real_name' : self.real_name,
            'universe' : self.universe,  
            'image' : self.image,
            'status' : self.status,
            'gender' : self.gender,
            'debut' : self.debut,
            'aliases' : self.aliases
            }


class Teams(db.Model):

    """
    DC teams with attributes title, first comic appeared in,
    and other information
    """

    __tablename__ = 'teams'

    id = db.Column(db.Integer)
    title = db.Column(db.String(100), primary_key=True)
    image = db.Column(db.String(250))
    debut = db.Column(db.String(100))
    origin = db.Column(db.String(100))
    identity = db.Column(db.String(100))
    status = db.Column(db.String(25))
    creators = db.Column(ARRAY(db.String(100)))
    universe = db.Column(ARRAY(db.String(100)))
    team_leaders = db.Column(ARRAY(db.String(100)))
    enemies = db.Column(ARRAY(db.String(100)))

    def __init__(self, title, image, debut, origin, identity, status, creators, universe, team_leaders, enemies):
        """
        Initialize a team
        """
        self.title = title
        self.image = image
        self.debut = debut
        self.origin = origin
        self.identity = identity
        self.status = status
        self.creators = creators
        self.universe = universe
        self.team_leaders = team_leaders
        self.enemies = enemies

    def __repr__(self):
        """
        Return represenation of this team in format
        <title {}> where {} is the team's title
        """
        return '<title {}>'.format(self.title)

    def to_json(self, list_view = False):
        """
        Return a dictionary of information of this teams
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'debut' : self.debut,
            'origin' : self.origin,
            'identity' : self.identity,
            'status' : self.status,
            'creators': self.creators,
            'universe': self.universe,
            'team_leaders' : self.team_leaders,
            'enemies' : self.enemies
        }

class Comics(db.Model):

    """
    DC comics with attributes title, issue number, writer, date
    published, and other information
    """

    __tablename__ = 'comics'

    id = db.Column(db.Integer)
    image = db.Column(db.String(250))
    title = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(50))
    locations = db.Column(ARRAY(db.String(100)))
    featured_characters = db.Column(ARRAY(db.String(100)))
    creators = db.Column(ARRAY(db.String(100)))

    def __init__(self, image, title, date, locations, featured_characters, creators):
        """
        Initialize a comic
        """
        self.image = image
        self.title = title
        self.date = date
        self.locations = locations
        self.featured_characters = featured_characters
        self.creators = creators

    def __repr__(self):
        """
        Return represenation of this comic in format
        <title {}> where {} is the comic's title
        """
        return '<title {}>'.format(self.title)

    def to_json(self, list_view = False):
        """
        Return a dictionary of information of this comic
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'image' : self.image,
            'date' : self.date,
            'locations' : self.locations,
            'featured_characters' : self.featured_characters,
            'creators' : self.creators
        }


class Movies(db.Model):

    """
    DC movies with attributes title, director, date released,
    and other information
    """

    __tablename__ = 'movies'

    id = db.Column(db.Integer)
    image = db.Column(db.String(250))
    title = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(50))
    running_time = db.Column(db.String(50))
    budget = db.Column(db.String(50))
    creators = db.Column(ARRAY(db.String(50)))
    featured_characters = db.Column(ARRAY(db.String(100)))

    def __init__(self, image, title, date, running_time, budget, creators, featured_characters):
        """
        Initialize a movie
        """
        self.image = image
        self.title = title
        self.date = date
        self.running_time = running_time
        self.budget = budget
        self.creators = creators
        self.featured_characters = featured_characters

    def __repr__(self):
        """
        Return represenation of this movie in format
        <title {}> where {} is the movie's title
        """
        return '<title {}>'.format(self.title)

    def to_json(self, list_view = False):
        """
        Return a dictionary of information of this movie
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'image' : self.image,
            'date' : self.date,
            'running_time' : self.running_time,
            'budget' : self.budget,
            'featured_characters' : self.featured_characters,
            'creators' : self.creators
        }

class Shows(db.Model):

    """
    DC shows with attributes title, network aired on, date first
    aired on, and other information
    """

    __tablename__ = 'shows'

    id = db.Column(db.Integer)
    title = db.Column(db.String(100), primary_key=True)
    last_air  = db.Column(db.String(250))
    running_time  = db.Column(db.String(250))
    image = db.Column(db.String(250))
    first_air = db.Column(db.String(50))
    creators = db.Column(ARRAY(db.String(100)))
    characters = db.Column(ARRAY(db.String(100)))

    def __init__(self, image, title, network, running_time, first_air, creators, characters, last_air):
        """
        Initialize a show
        """
        self.image = image
        self.title = title
        self.last_air  = last_air
        self.running_time  = running_time
        self.first_air = first_air
        self.creators = creators
        self.characters = characters

    def __repr__(self):
        """
        Return represenation of this show in format
        <title {}> where {} is the show's title
        """
        return '<title {}>'.format(self.title)

    def to_json(self, list_view = False):

        """
        Return a dictionary of information of this movie
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'last_air' : self.last_air,
            'running_time' : self.running_time,
            'first_air' : self.first_air,
            'creators' : self.creators,
            'characters' : self.characters,
            'image' : self.image
        }

class Creators(db.Model):

    """
    DC creators with attirubtes title, occupation, birth date, birth place
    first publication made (if applicable), and other information
    """

    __tablename__ = 'creators'

    id = db.Column(db.Integer)
    title = db.Column(db.String(50), primary_key=True)
    ocupations = db.Column(ARRAY(db.String(50)))
    gender = db.Column(String(50))
    birth_date = db.Column(db.String(50))
    first_publication = db.Column(db.String(100))
    employers = db.Column(ARRAY(db.String(100)))

    def __init__(self, title, occupations, birth_date, first_publication, employers):        
        """
        Initialize a creator
        """
        self.title = title
        self.occupations = occupations
        self.birth_date = birth_date
        self.first_publication = first_publication
        slef.employers = db.Column(ARRAY(db.String(100)))

    def __repr__(self):
        """
        Return represenation of this creator in format
        <title {}> where {} is the creator's title
        """
        return '<title {}>'.format(self.title)

    def to_json(self, list_view = False):
        """
        Return a dictionary of information of this movie
        """
        return {
            'id' : self.id,
            'title' : self.title,
            'birth_date' : self.birth_date,
            'gender' : self.gender,
            'first_publication' : self.first_publication,
            'employers' : self.employers
        }