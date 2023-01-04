from mongoengine import Document, StringField , IntField

class Blogs(Document):
    title = StringField()
    author = StringField()
    body = StringField()
    likes = IntField()
    dislikes = IntField()