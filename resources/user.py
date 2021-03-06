import sqlite3
from sqlite3.dbapi2 import DataError
from typing import Text
from flask_restful import Resource , reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username' ,
            type=str,
            required = True,
            help = 'This field couldn\'t be blank' 
    )    
    parser.add_argument('password' ,
            type=str,
            required = True,
            help = 'This field couldn\'t be blank' 
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_name(data['username']):
            return {'message': "User Exists!"}, 400

        item = UserModel(data['username'] , data['password'])
        item.save_to_db()

        return {'message': 'User Created!'} , 201
