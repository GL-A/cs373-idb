import os
import sys
from models import Character, Teams, Shows, Movies, Comics, Creators, db
from models import characters_schema, teams_schema, movies_schema, shows_schema, comics_schema, creators_schema
from models import character_schema, team_schema, movie_schema, show_schema, comic_schema, creator_schema
from sqlalchemy.exc import IntegrityError
from flask_restful import Api, Resource
from flask import jsonify
from dc import api

 
#The following class will be used for GET and POST requests to /users
class CharacterList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all users
        character_query = Character.query.all()
        #Serialize the query results in the JSON API format
	char_scheme = characters_schema.dump(character_query)
        results = jsonify(char_scheme.data)
        return results

#The following class will be used for GET and POST requests to /teams
class TeamsList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all teams
        teams_query = Teams.query.all()
        #Serialize the query results in the JSON API format
	team_scheme = teams_schema.dump(teams_query)
        results = jsonify(team_scheme.data)
        return results

#The following class will be used for GET and POST requests to /comics
class ComicsList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all comics
        comics_query = Comics.query.all()
        #Serialize the query results in the JSON API format
        comic_scheme = comics_schema.dump(comics_query)
        results = jsonify(comic_scheme.data)
        return results

#The following class will be used for GET and POST requests to /movies
class MoviesList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all movies
        movies_query = Movies.query.all()
        #Serialize the query results in the JSON API format
        movie_scheme = movies_schema.dump(movies_query)
        results = jsonify(movie_scheme.data)
        return results

#The following class will be used for GET and POST requests to /users
class ShowsList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all users
        shows_query = Shows.query.all()
        #Serialize the query results in the JSON API format
        show_scheme = shows_schema.dump(shows_query)
        results = jsonify(show_scheme.data)
        return results

#The following class will be used for GET and POST requests to /users
class CreatorsList(Resource):
       #Function for a GET request
       def get(self):
        #Query the database and return all users
        creators_query = Creators.query.all()
        #Serialize the query results in the JSON API format
	create_scheme = creators_schema.dump(creators_query)
        results = jsonify(create_scheme.data)
        return results


#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /character/<str:id>.json
class CharacterUpdate(Resource):
 

    def get(self, id):  
        try:
            character_query = Character.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Character could not be found."}), 404
        result = character_schema.dump(character_query)
        return jsonify(result.data)
 
#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /teams/<string:id>.json
class TeamsUpdate(Resource):
    def get(self, id):
        try:
            team_query = Teams.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Team could not be found."}), 404
        result = team_schema.dump(team_query)
        return jsonify(result.data)

#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /shows/<string:id>.json
class ShowsUpdate(Resource):
    def get(self, id):
        try:
            show_query = Shows.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Show could not be found."}), 404
        result = show_schema.dump(show_query)
        return jsonify(result.data)

#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /movies/<string:id>.json
class MoviesUpdate(Resource):
    def get(self, id):
        try:
            movie_query = Movies.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Movie could not be found."}), 404
        result = movie_schema.dump(movie_query)
        return jsonify(result.data)

#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /comics/<string:id>.json
class ComicsUpdate(Resource):
    def get(self, id):
        try:
            comic_query = Comics.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Comic could not be found."}), 404
        result = comic_schema.dump(comic_query)
        return jsonify(result.data)

#The following class is used when a GET,PATCH,DELETE HTTP request is sent to /creators/<string:id>.json
class CreatorsUpdate(Resource):
    def get(self, id):
        try:
            creator_query = Creators.query.get(id.replace("_", " "))
        except IntegrityError:
            return jsonify({"message": "Creator could not be found."}), 404
        result = creator_schema.dump(creator_query)
        return jsonify(result.data)








