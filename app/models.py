#-----------
# imports
#-----------


from flask import Flask
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError, pre_load
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.jsontools import JsonSerializableBase
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable
from sqlalchemy_fulltext import FullText, FullTextSearch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

make_searchable()

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:psql@localhost:5432/dcdatabase'
db = SQLAlchemy(app)
db.init_app(app)


# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('postgresql://postgres:psql@localhost:5432/dcdatabase')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

Base = declarative_base(cls=(JsonSerializableBase,))


"""
The Models module. 

pydoc -w models
"""

class CharacterQuery(BaseQuery, SearchQueryMixin):
    pass

class TeamsQuery(BaseQuery, SearchQueryMixin):
    pass

class MoviesQuery(BaseQuery, SearchQueryMixin):
    pass

class ShowsQuery(BaseQuery, SearchQueryMixin):
    pass

class CreatorsQuery(BaseQuery, SearchQueryMixin):
    pass

class ComicsQuery(BaseQuery, SearchQueryMixin):
    pass

#-----------
# Characters
#-----------

#TODO: add category attribute for models, and search_vector for each model
#ALSO need to check configure_mappers before the creationg of tables. Need to ask andrew about how the db works in relation with that

class Character(db.Model, Base):

    """
    DC characters with attributes title, hero/villain alias, an image,
    their alignment, and other information
    """
    __tablename__ = 'characters'
    query_class = CharacterQuery
    title = db.Column(db.String(50), primary_key=True)
    image = db.Column(db.String(250))
    universes = db.Column(ARRAY(db.String(100)))
    gender = db.Column(db.String(50))
    aliases = db.Column(ARRAY(db.String(100)))
    creators = db.Column(ARRAY(db.String(100)))
    identity = db.Column(db.String(50))
    real_name = db.Column(db.String(50))
    debut = db.Column(db.String(50))
    affiliation = db.Column(ARRAY(db.String(100)))
    alignment = db.Column(db.String(50))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'universes', 'gender', 'aliases', 'creators', 'identity', 'real_name', 'debut', 'affiliation', 'alignment', 'category'))

    def __init__(self, title="", alias=[], image="", alignment="", creators=[], identity="", real_name="", universe=[], status="", gender="", debut="", aliases=[], affiliation=[]):
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
        self.universes = universe
        self.gender = gender
        self.debut = debut
        self.affiliation = affiliation




#-----------
# Teams
#-----------


class Teams(db.Model, Base):

    """
    DC teams with attributes title, first comic appeared in,
    and other information
    """
    __tablename__ = 'teams'
    query_class = TeamsQuery
    title = db.Column(db.String(100), primary_key=True)
    image = db.Column(db.String(250))
    debut = db.Column(db.String(100))
    identity = db.Column(db.String(100))
    status = db.Column(db.String(25))
    creators = db.Column(ARRAY(db.String(100)))
    universes = db.Column(ARRAY(db.String(100)))
    team_leaders = db.Column(ARRAY(db.String(100)))
    enemies = db.Column(ARRAY(db.String(100)))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'debut', 'identity', 'status', 'creators', 'universes', 'team_leaders', 'enemies', 'category'))

    def __init__(self, title, image, debut, identity, status, creators, universe, team_leaders, enemies):
        """
        Initialize a team
        """
        self.title = title
        self.image = image
        self.debut = debut
        self.identity = identity
        self.status = status
        self.creators = creators
        self.universes = universe
        self.team_leaders = team_leaders
        self.enemies = enemies

#-----------
# Comics
#-----------


class Comics(db.Model):

    """
    DC comics with attributes title, issue number, writer, date
    published, and other information
    """
    __tablename__ = 'comics'
    query_class = ComicsQuery
    image = db.Column(db.String(250))
    title = db.Column(db.String(100), primary_key=True)
    release_date = db.Column(db.String(50))
    locations = db.Column(ARRAY(db.String(100)))
    featured_characters = db.Column(ARRAY(db.String(100)))
    creators = db.Column(ARRAY(db.String(100)))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'release_date', 'locations', 'featured_characters', 'creators', 'category'))

    def __init__(self, image, title, release_date, locations, featured_characters, creators):
        """
        Initialize a comic
        """
        self.image = image
        self.title = title
        self.release_date = date
        self.locations = locations
        self.featured_characters = featured_characters
        self.creators = creators


#-----------
# Movies
#-----------


class Movies(db.Model):

    """
    DC movies with attributes title, director, date released,
    and other information
    """
    __tablename__ = 'movies'
    query_class = MoviesQuery
    image = db.Column(db.String(250))
    title = db.Column(db.String(100), primary_key=True)
    release_date = db.Column(db.String(50))
    running_time = db.Column(db.String(50))
    budget = db.Column(db.String(50))
    creators = db.Column(ARRAY(db.String(50)))
    featured_characters = db.Column(ARRAY(db.String(100)))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'release_date', 'running_time', 'budget', 'creators', 'featured_characters', 'category'))

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


#-----------
# Shows
#-----------


class Shows(db.Model):

    """
    DC shows with attributes title, network aired on, date first
    aired on, and other information
    """
    __tablename__ = 'shows'
    query_class = ShowsQuery
    title = db.Column(db.String(100), primary_key=True)
    last_air_date = db.Column(db.String(250))
    running_time = db.Column(db.String(250))
    image = db.Column(db.String(250))
    first_air_date = db.Column(db.String(50))
    creators = db.Column(ARRAY(db.String(100)))
    featured_characters = db.Column(ARRAY(db.String(100)))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'first_air_date', 'last_air_date','running_time', 'creators', 'featured_characters', 'category'))


    def __init__(self, image, title, running_time, first_air_date, creators, featured_characters, last_air_date):
        """
        Initialize a show
        """
        self.image = image
        self.title = title
        self.last_air_date = last_air_date
        self.running_time = running_time
        self.first_air_date = first_air_date
        self.creators = creators
        self.featured_character = featured_characters


#-----------
# Creators
#-----------


class Creators(db.Model):

    """
    DC creators with attirubtes title, occupation, birth date, birth place
    first publication made (if applicable), and other information
    """
    __tablename__ = 'creators'
    query_class = CreatorsQuery
    title = db.Column(db.String(50), primary_key=True)
    image = db.Column(String(50))
    job_titles = db.Column(ARRAY(db.String(50)))
    gender = db.Column(String(50))
    birth_date = db.Column(db.String(50))
    first_publication = db.Column(db.String(100))
    employers = db.Column(ARRAY(db.String(100)))
    creations = db.Column(ARRAY(db.String(100)))
    category = db.Column(db.String(50))
    search_vector = db.Column(TSVectorType('title', 'image', 'job_titles', 'gender', 'birth_date', 'first_publication', 'employers', 'creations', 'category'))


    def __init__(self, title, occupations, birth_date, first_publication, employers, creations):
        """
        Initialize a creator
        """
        self.title = title
        self.occupations = occupations
        self.birth_date = birth_date
        self.first_publication = first_publication
        self.employers = employers
        self.creations = creations


# SCHEMA###

class CharacterSchema(Schema):
    """
    Schema the Characters table must conform to.
    """
    title = fields.Str(dump_only=True)
    image = fields.Str()
    universes = fields.List(fields.Raw)
    gender = fields.Str()
    aliases = fields.List(fields.Raw)
    creators = fields.List(fields.Raw)
    identity = fields.Str()
    real_name = fields.Str()
    debut = fields.Str()
    affiliation = fields.List(fields.Raw)
    alignment = fields.Str()
    category = fields.Str()

class AmbiguousSchema(Schema):
    """
    Schema the ambiguous table must conform to.
    """
    title = fields.Str(dump_only=True)
    category = fields.Str()
    related = fields.List(fields.Raw)
    


class TeamsSchema(Schema):
    """
    Schema the Teams table must conform to.
    """

    title = fields.Str(dump_only=True)
    image = fields.Str()
    debut = fields.Str()
    identity = fields.Str()
    status = fields.Str()
    creators = fields.List(fields.Raw)
    universes = fields.List(fields.Raw)
    team_leaders = fields.List(fields.Raw)
    enemies = fields.List(fields.Raw)
    category = fields.Str()


class ComicsSchema(Schema):
    """
    Schema the Comics table must conform to.
    """

    title = fields.Str(dump_only=True)
    image = fields.Str()
    release_date = fields.Str()
    locations = fields.List(fields.Raw)
    featured_characters = fields.List(fields.Raw)
    creators = fields.List(fields.Raw)
    category = fields.Str()


class MoviesSchema(Schema):
    """
    Schema the Movies table must conform to.
    """

    title = fields.Str(dump_only=True)
    image = fields.Str()
    release_date = fields.Str()
    running_time = fields.Str()
    budget = fields.Str()
    creators = fields.List(fields.Raw)
    featured_characters = fields.List(fields.Raw)
    category = fields.Str()


class ShowsSchema(Schema):
    """
    Schema the Shows table must conform to.
    """

    title = fields.Str(dump_only=True)
    image = fields.Str()
    last_air_date = fields.Str()
    running_time = fields.Str()
    first_air_date = fields.Str()
    creators = fields.List(fields.Raw)
    featured_characters = fields.List(fields.Raw)
    category = fields.Str()


class CreatorsSchema(Schema):
    """
    Schema the Creators table must conform to.
    """

    title = fields.Str(dump_only=True)
    image = fields.Str()
    job_titles = fields.List(fields.Raw)
    gender = fields.Str()
    birth_date = fields.Str()
    first_publication = fields.Str()
    employers = fields.List(fields.Raw)
    creations = fields.List(fields.Raw)
    category = fields.Str()

# Custom validator


def must_not_be_blank(data):
    """
    Check to ensure data is provided
    """
    if not data:
        raise ValidationError('Data not provided.')


characters_schema = CharacterSchema(many=True)
teams_schema = TeamsSchema(many=True)
comics_schema = ComicsSchema(many=True)
movies_schema = MoviesSchema(many=True)
shows_schema = ShowsSchema(many=True)
creators_schema = CreatorsSchema(many=True)
ambiguous_schema = AmbiguousSchema(many=True)


character_schema = CharacterSchema()
team_schema = TeamsSchema()
comic_schema = ComicsSchema()
movie_schema = MoviesSchema()
show_schema = ShowsSchema()
creator_schema = CreatorsSchema()
ambiguous_schema = AmbiguousSchema()
