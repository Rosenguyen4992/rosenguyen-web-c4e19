from flask import Flask, render_template
from models.service import Service
import mlab
import bson

app = Flask(__name__)

mlab.connect()
#mongoengine


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender, yob__lte=1998, address__icontains="Nội")
    return render_template('search.html', all_service = all_service)

deleteobj = Service.objects.first
deleteobj.delete()


if __name__ == '__main__':
    app.run(debug=True)
 