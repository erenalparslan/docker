from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests





app = Flask(__name__)

api = Api(app)



class Users(Resource):

   def get(self, sayi):
        if sayi == '0':
            return {'message': 'Number is not equal to 0.'}, 401

        url = "https://meowfacts.herokuapp.com/?count=" + str(sayi)

        response = requests.get(url)

        data = response.json()


        return {'data': data['data']}, 200



   def post(self):

       name = request.args['name']

       age = request.args['age']

       city = request.args['city']



       req_data = pd.DataFrame({

           'name'      : [name],

           'age'       : [age],

           'city'      : [city]

       })

       data = pd.read_csv('users.csv')


       data = data.append(req_data, ignore_index=True)

       data.to_csv('users.csv', index=False)

       return {'message' : 'Record successfully added.'}, 201





class Name(Resource):

   def get(self,name):

       data = pd.read_csv('users.csv')

       data = data.to_dict('records')

       for entry in data:

           if entry['name'] == name :

               return {'data' : entry}, 200

       return {'message' : 'No entry found with this name !'}, 400



api.add_resource(Users, '/users/<string:sayi>')

api.add_resource(Name, '/isim/<string:name>')





if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000)

   app.run()

