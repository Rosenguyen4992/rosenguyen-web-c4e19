from mongoengine import *
import mlab

mlab.connect()

# design database
class Video(Document):
    link = StringField()
    title = StringField()
    view = IntField()
    thumbnail = StringField()
    youtubeid = StringField()
