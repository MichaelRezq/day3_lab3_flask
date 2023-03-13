
from flask import  Blueprint

posts_blueprint= Blueprint('posts', __name__, url_prefix='/')

from app.posts import views