from mongoengine import *
import mlab

mlab.connect()

# design database
class Order(Document):
    service_id = StringField()
    user_id = StringField()
    time = ComplexDateTimeField()
    is_accept = BooleanField()
