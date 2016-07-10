import os

from flask import *
from models import *

# --------------
# Views
# --------------

@app_instance.route('/', methods=['GET'])
def index():
  return send_file('index.html')

# --------------
# RESTful app_instance
# --------------

@app_instance.route('/api/characters/<int:page>', methods=['GET'])
@app_instance.route('/api/characters', methods=['GET'])
def get_characters(page=1):
    request = Character.query.paginate(page=page, per_page=25)
    characters = request.items
    return jsonify({'characters':[character.to_json() for character in characters]})

@app_instance.route('/api/teams/<int:page>', methods=['GET'])
@app_instance.route('/api/teams', methods=['GET'])
def get_teams(page=1):
    request = Teams.query.paginate(page=page, per_page=25)
    teams = request.items
    return jsonify({'teams':[team.to_json() for team in teams]})

@app_instance.route('/api/comics/<int:page>', methods=['GET'])
@app_instance.route('/api/comics', methods=['GET'])
def get_comics(page=1):
    request = Comics.query.paginate(page=page, per_page=25)
    comics = request.items
    return jsonify({'comics':[comic.to_json() for comic in comics]})

@app_instance.route('/api/movies/<int:page>', methods=['GET'])
@app_instance.route('/api/movies', methods=['GET'])
def get_movies(page=1):
    request = Movies.query.paginate(page=page, per_page=25)
    movies = request.items
    return jsonify({'movies':[movie.to_json() for movie in movies]})

@app_instance.route('/api/Shows/<int:page>', methods=['GET'])
@app_instance.route('/api/Shows', methods=['GET'])
def get_characters(page=1):
    request = Shows.query.paginate(page=page, per_page=25)
    shows = request.items
    return jsonify({'shows':[show.to_json() for show in shows]})

@app_instance.route('/api/Creators/<int:page>', methods=['GET'])
@app_instance.route('/api/Creators', methods=['GET'])
def get_characters(page=1):
    request = Creators.query.paginate(page=page, per_page=25)
    creators = request.items
    return jsonify({'creators':[creator.to_json() for creator in creators]})

#-----------------
# Individual pages
#-----------------

@app_instance.route('/api/characters/<int:id>', methods=['GET'])
def get_character(id):
  request = Character.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.route('/api/teams/<int:id>', methods=['GET'])
def get_team(id):
  request = Team.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.route('/api/comics/<int:id>', methods=['GET'])
def get_comic(id):
  request = Comic.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id):
  request = Movie.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.route('/api/shows/<int:id>', methods=['GET'])
def get_show(id):
  request = Show.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.route('/api/creators/<int:id>', methods=['GET'])
def get_creator(id):
  request = Creator.query.filter_by(id=id).first()
  if request is None:
    abort(404)
  return jsonify(request.to_json(list_view=True))

@app_instance.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)
