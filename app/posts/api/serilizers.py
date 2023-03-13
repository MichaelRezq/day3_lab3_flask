from flask_restful import fields
CategorySerilizer= {
    'id': fields.Integer,
    'cat_id': fields.String,
}



postserilizer= {
    'id':fields.Integer,
    'title' :fields.String,
    'body': fields.String,
    'category': fields.Nested(CategorySerilizer)
}