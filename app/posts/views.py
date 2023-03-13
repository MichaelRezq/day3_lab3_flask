from app.models import Post
from flask import  render_template, redirect, url_for,request
from app.models import Post,Categorey
from  app.models import  db
from .forms import PostForm,CategoryForm


from app.posts import  posts_blueprint
from app.categorey import  categories_blueprint

@posts_blueprint.route('test')
def testfunction():
    return '<h1> Posts Index </h1>'


@posts_blueprint.route('')
def posts_index():
    posts = Post.get_all_posts()

    return render_template('Posts/index.html', posts=posts)


@posts_blueprint.route('/<int:id>')
def post_info(id):
    post = Post.query.get_or_404(id)
    return render_template('Posts/show.html',post=post)

@posts_blueprint.route('/createpost', methods = ['POST','GET'],endpoint="createpost")
def create_post():
    form = PostForm()
    if request.method == 'GET':
        return render_template("Posts/createpost.html", form=form, category=Categorey.query.all())
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        record = Post(title=title,
                      body=body,
                      cat_id=category)

        db.session.add(record)
        db.session.commit()
        return redirect('/')

@posts_blueprint.route('/editpost/<int:id>/', methods=('GET', 'POST'),endpoint="editpost")
def editpost(id):
    post=Post.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        post.title=title
        post.body=body
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('Posts/UpdatePost.html',post=post)





@posts_blueprint.route('/<int:id>/delete', endpoint='delete')
def post_delete(id):
    post = Post.query.get_or_404(id)
    res =post.delete_object()
    if res :
        return redirect(url_for("posts.posts_index"))
