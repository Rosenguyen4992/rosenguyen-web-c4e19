from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()

all_service.delete({})

print ("Done")

# first_service = all_service[0]

# print(first_service['yob'])

# id_to_find = "5b5b25b6c25c1356387ec674"

# # id = Service.objects(id=id_to_find) # => list []
# id = Service.objects.get(id=id_to_find) # => object
# # id = Service.objects.with_id(id_to_find) # => object

# # print (id.to_mongo())
# if id is not None:
#     id.delete()
#     print("Deleted")

    # # update
    # print ("Before", id.to_mongo())
    # id.update(set__name="Someone", set__yob=1990)
    # id.reload()
#     # print ("After", id.to_mongo())
# else:
#     print("Not found")

