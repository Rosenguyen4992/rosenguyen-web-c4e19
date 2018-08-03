from mongoengine import *
import web2_mlab

web2_mlab.connect()

# design database
class Service2(Document): 
    name = StringField()
    gender = IntField()
    email = StringField()
    phonenumber = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
