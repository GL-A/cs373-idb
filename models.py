from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

"""
Using the intergalactic db source code as reference
as well as flask-sqalchemy.pocoo.org quickstart guide
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/dcdatabase'
db = SQLAlchemy(app)

class Character(db.Model):
  """
  DC characters with attributes name, hero/villain alias, an image,
  their alignment, and other information
  """

  __tablename__ = 'characters'

  id = Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  alias = db.Column(db.String(50))
  image = db.Column(db.String(250))
  alignment = db.Column(db.String(50))

  def __init__(self, name, alias, image, alignment):
    """
    Initialize the character
    """
    self.name = name
    self.alias = alias
    self.image = image
    self.alignment = alignment

  def __repr__(self):
    """
    Return represenation of this character in format
    <name {}> where {} is character's name
    """
    return '<name {}>'.format(self.name)

class Teams(db.Model):
  """
  DC teams with attributes name, first comic appeared in,
  and other information
  """

  __tablename__ = 'teams'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  image = db.Column(db.String(250))
  first_appearance = db.Column(db.String(100))
  base_of_operations = db.Column(db.String(100))

  def __init__(self, name, image, first_appearance, base_of_operations):
    self.name = name
    self.image = image
    self.first_appearance = first_appearance
    self.base_of_operations = base_of_operations

  def __repr__(self):
    return '<name {}>'.format(self.name)

class Comics(db.Model):
  """
  DC comics with attributes name, issue number, writer, date
  published, and other information
  """

  __tablename__ = 'comics'

  id = db.Column(db.Integer, primary_key=True)
  image = db.Column(db.String(250))
  name = db.Column(db.String(100))
  issue = db.Column(db.String(5))
  date = db.Column(db.String(50))
  writer = db.Column(db.String(50))

  def __init__(self, image, name, issue, date, writer):
    self.image = image
    self.name = name
    self.issue = issue
    self.date = date
    self.writer = writer

  def __repr__(self):
    return '<name {}>'.format(self.name)

class Movies(db.Model):
  """
  DC movies with attributes name, director, date released,
  and other information
  """

  __tablename__ = 'movies'

  id = db.Column(db.Integer, primary_key=True)
  image = db.Column(db.String(250))
  name = db.Column(db.String(100))
  director = db.Column(db.String(50))
  date = db.Column(db.String(50))
  distributors = db.Column(db.String(30))
  distributors = db.Column(db.String(50))

  def __init__(self, image, name, director, date, distributors, composers):
    self.image = image
    self.name = name
    self.director = director
    self.date = date
    self.distributors = distributors
    self.composers = composers

  def __repr__(self):
    return '<name {}>'.format(self.name)

class Shows(db.Model):
  """
  DC shows with attributes name, network aired on, date first
  aired on, and other information
  """

  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key=True)
  image = db.Column(db.String(250))
  name = db.Column(db.String(100))
  network = db.Column(db.String(50))
  date = db.Column(db.String(50))

  def __init__(self, image, name, network, date):
    self.image = image
    self.name = name
    self.network = network
    self.date = date

  def __repr__(self):
    return '<name {}>'.format(self.name)

class Creators(db.Model):
  """
  DC creators with attirubtes name, occupation, birth date, birth place
  first publication made (if applicable), and other information
  """

  __tablename__ = 'creators'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  ocupation = db.Column(db.String(50))
  birth_year = db.Column(db.String(50))
  birth_place = db.Column(db.String(200))
  first_publication = db.Column(db.String(100))

  def __init__(self, name, occupation, birth_year, birth_place, first_publication):
    self.name = name
    self.occupation = occupation
    self.birth_year = birth_year
    self.birth_place = birth_place
    self.first_publication = first_publication

  def __repr__(self):
    return '<name {}>'.format(self.name)