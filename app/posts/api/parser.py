from flask_restful import  reqparse

postparser = reqparse.RequestParser()

postparser.add_argument('title', type=str,help='Title is required', required=True )
postparser.add_argument('body', type=str,help='Body is required' ,required=True )
