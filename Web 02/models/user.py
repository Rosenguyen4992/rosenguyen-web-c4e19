from mongoengine import *
import mlab

mlab.connect()

# design database
class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    fullname = StringField()
