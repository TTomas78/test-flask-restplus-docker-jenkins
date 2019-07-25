import os
import importlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate,MigrateCommand

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    with app.app_context():
        db.init_app(app)
        return app

db = SQLAlchemy()
app = create_app('Config')
api = Api(app)
migrate = Migrate(app,db)

from models import *

class HelloWorld(Resource):
    
    def get(self):
            
        return {'hello': 'people!'}
api.add_resource(HelloWorld, '/')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
