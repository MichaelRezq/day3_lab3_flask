from flask import render_template,request,redirect
from app.models import Categorey
from app.categorey import  categories_blueprint
from app.posts.forms import CategoryForm
from  app.models import  db

@categories_blueprint.route('/')
def department_index():
    categories = Categorey.get_all_categories()
    return render_template('categorey/index.html',categories=categories )

@categories_blueprint.route('/createcategorey', methods = ['POST','GET'],endpoint="createcategorey")
def addNewCategory():
    form = CategoryForm()
    if request.method == 'GET':
        return render_template("categorey/createcategorey.html",form=form)
    if request.method == 'POST':
        print(request.form)
        category = request.form['categoryName']
        record = Categorey(name=category)
        db.session.add(record)
        db.session.commit()
        return redirect('/categories')
