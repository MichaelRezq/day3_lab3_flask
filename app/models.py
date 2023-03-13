
from flask_sqlalchemy import SQLAlchemy
from  datetime import  datetime
db = SQLAlchemy()

class Categorey(db.Model):
    __tablename__= 'categorey'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ##### db.relationship("ModelName", -----)
    posts = db.relationship('Post', backref='categorey', lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()


class Post(db.Model):
    __tablename__ = 'posts'
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.String(1000))
    image=db.Column(db.String(300))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    ############################### db.foreignkey(table_name.id)
    cat_id = db.Column(db.Integer, db.ForeignKey('categorey.id'), nullable= True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()


    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True
