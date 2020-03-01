'''
Created on 19 февр. 2020 г.

@author: mcghost
'''

from models import Post

def change_query(old_query):
    parameters = ( Post.title.contains(old_query) |
               Post.body.contains(old_query) |
               Post.title.contains(old_query.upper()) |
               Post.title.contains(old_query.lower()) |
               Post.title.contains(old_query.title()) )
    new_query = Post.query.filter(parameters)
    return new_query    
    
    
            
    