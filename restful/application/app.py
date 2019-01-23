import logging
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from application.models.db import db
from application.schemas.marshmallow import ma


# ***** Import Resource Classes ***** #
from application.resources.user import User, Users

dir = os.path.dirname(__file__)
def create_app(config_name):

    app = Flask(__name__)
    app.config.from_envvar(config_name)
    db.init_app(app)
    ma.init_app(app)

    api = Api(app)

    # ***** Error Handling and Logging ***** #
    logging.basicConfig(filename = 'debug.log', level = logging.DEBUG)

    # ***** Define Endpoints ***** #
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user/<int:id>', '/user')

    @app.after_request
    def after_request(response):
        response.headers.set('Access-Control-Expose-Headers', 'Link')
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response
    
    return app

app = create_app('dev')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3001")