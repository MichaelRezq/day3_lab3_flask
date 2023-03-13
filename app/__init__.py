

from flask import  Flask
from flask_migrate import Migrate
from  app.models import  db
from app.config import  projectConfig as AppConfig   # this dict
from app.posts.api.api_views import AllPosts,PostGetSpecificAndUpdateAndDelete
from flask_restful import Api

def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config # search in this class about class variable with this name
    app.config['SECRET_KEY'] = current_config.SECRET_KEY

    app.config.from_object(current_config)
    db.init_app(app)

    ## add migration
    migrate = Migrate(app, db,render_as_batch=True)

    ### add route
    # from app.students.views import testfunction,students_index, student_info, student_delete
    # from app.students.errors import page_not_found
    # from app.departments.views import department_index
    #
    #
    # app.add_url_rule('/test', view_func=testfunction)
    # app.register_error_handler(404, page_not_found)
    # app.add_url_rule('/students', view_func=students_index)
    # app.add_url_rule('/students/<id>', view_func=student_info)
    # app.add_url_rule('/students/<id>/delete', view_func=student_delete)

    #################### blueprints
    from app.categorey import categories_blueprint
    from app.posts import posts_blueprint
    # app.add_url_rule('/departments', view_func=department_index, endpoint='departments_all')
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(posts_blueprint)

    api = Api(app)
    api.add_resource(AllPosts, '/api/posts')
    api.add_resource(PostGetSpecificAndUpdateAndDelete, '/api/posts/<int:id>')

    return  app



