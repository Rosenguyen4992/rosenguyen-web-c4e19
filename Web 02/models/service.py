from mongoengine import *
import mlab

mlab.connect()

# design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# # new_service = Service(
# #     name = "Linh Ka",
# #     yob = 2000,
# #     gender = 0,
# #     height = 150,
# #     phone = "9913782793",
# #     address = "Đống Đa, Hà Nội",
# #     status = False
# # )

# new_service.save()
