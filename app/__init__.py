import os
import sys
from flask_restful import Api, Resource
from flask import Flask, send_file, send_from_directory, safe_join, request, Response, abort

app = Flask(__name__)
api = Api(app)
app._static_folder = "/var/www/dc/dc/static/"
from rest import *




@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(**kwargs):
    return send_file('index.html')

#Define API endpoints
#Map classes to API endpoints
api.add_resource(CharacterList, '/characters.json')
api.add_resource(TeamsList, '/teams.json')
api.add_resource(ShowsList, '/shows.json')
api.add_resource(MoviesList, '/movies.json')
api.add_resource(ComicsList, '/comics.json')
api.add_resource(CreatorsList, '/creators.json')
api.add_resource(CharacterUpdate, '/characters/<string:id>.json')
api.add_resource(TeamsUpdate, '/teams/<string:id>.json')
api.add_resource(ShowsUpdate, '/shows/<string:id>.json')
api.add_resource(MoviesUpdate, '/movies/<string:id>.json')
api.add_resource(ComicsUpdate, '/comics/<string:id>.json')
api.add_resource(CreatorsUpdate, '/creators/<string:id>.json')

if __name__ == "__main__":
    app.run()










