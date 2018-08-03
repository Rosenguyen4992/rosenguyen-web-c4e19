from models.service import Service2
import web2_mlab

web2_mlab.connect()

all_service = Service2.objects()