from models.service import Service2
import web2_mlab
from faker import Faker
from random import randint, choice


web2_mlab.connect()

fake = Faker()

for i in range (100):
    print("Saving service", i+1, "...")
    new_service = Service2 (
        name = fake.name(),
        gender = randint(0,1),
        email = fake.email(),
        phonenumber = fake.phone_number(),
        job = fake.job(),
        company = fake.job(),
        contacted = choice([False, True]),
    )
    new_service.save()