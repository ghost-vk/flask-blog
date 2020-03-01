'''
Created on 16 февр. 2020 г.

@author: mcghost
'''
from flask import Blueprint
from flask import render_template

from models import Post, Tag
from creation.forms import PostForm

from flask import request
from flask import redirect
from flask import url_for
from app import db

from assist import change_query

from flask_security import login_required



posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post) #Документация  wtforms класс Form
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():

    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = change_query(q)
    else:    
        posts = Post.query.order_by(Post.id.desc())  
    pages = posts.paginate(page, 5, False)
          
    return render_template('posts/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404() # здесь можно добавить уникальность
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first_or_404()
    posts = tag.posts.all()
    return render_template('/posts/tag_detail.html', tag=tag, posts=posts)











