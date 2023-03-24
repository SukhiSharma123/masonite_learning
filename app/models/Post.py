""" Post Model """

from masoniteorm.models import Model


class Post(Model):
    """Post Model"""

    __fillable__ = ['title', 'body']
    __table__ = 'posts'
