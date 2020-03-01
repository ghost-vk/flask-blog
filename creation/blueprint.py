from flask import Blueprint
from flask import render_template

from models import Post, Tag
from .forms import PostForm

from flask import request
from flask import redirect
from flask import url_for
from app import db

from assist import change_query

from flask_security import login_required

creation = Blueprint('creation', __name__, template_folder='templates')


@creation.route('/', methods=['POST', 'GET'])
@login_required
def create_post():
     
    if request.method == 'POST':       
        title = request.form['title']
        body = request.form['body']
        
        if title and body:           #если создать пустые посты, то slug=None
                 
            try:
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            except:
                print('Something wrong')
             
            return redirect(url_for('posts.index'))
     
     
    form = PostForm()
    return render_template('creation/create_post.html', form=form)