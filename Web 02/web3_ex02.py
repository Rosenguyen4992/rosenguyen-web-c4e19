from models.service import Service
import mlab
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()

des = [
    "ngoan hiền dễ thương",
    "yêu màu hồng, ghét sự giả dối",
    "nhà giàu chung thủy mỗi tội hay xạo ke" 
]

for i in range (90):
    print("Saving service", i+1, "...")
    v1 = 90 + randint(-10,10)
    v2 = 60 + randint(-10,10)
    v3 = 90 + randint(-10,10)
    new_service = Service (
        name = fake.name(),
        yob = randint(1990, 2000),
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([False, True]),
        description = choice(des),
        measurement = [ v1, v2, v3 ],
    )
    new_service.save()