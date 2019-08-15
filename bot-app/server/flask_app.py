from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
import requests
import json
import cluster_grab as cg

## Using code from https://github.com/narenaryan/Salary-API as starting template

app = Flask(__name__)
api = Api(app)

CORS(app, origins="*")

# Test Classes: Use these to ensure server is working
class Hello_World(Resource):
    def get(self):
        # Return string Hello World
        return {'Hello':  'world!'}


@app.route('/')
def index():
    return "Welcome to my Python Server" 

api.add_resource(Hello_World, '/helloworld')

if __name__ == '__main__':
     app.run(port='5002')
