'''
Created on 16 февр. 2020 г.

@author: mcghost
'''
from app import app
from app import db

from posts.blueprint import posts
from creation.blueprint import creation

import view


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(creation, url_prefix='/creation')

if __name__ == '__main__':
    app.run()