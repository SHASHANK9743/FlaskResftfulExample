from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app=app)


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Portfolio Python Services are up!!!!'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
