from flask import Flask, render_template
from models.service import Service2
import web2_mlab
import bson

app = Flask(__name__)

web2_mlab.connect()
#mongoengine


@app.route('/')
def index():
    return render_template('web2_index.html')

@app.route('/filter')
def filter():
    top10_service2 = Service2.objects(gender=1, contacted=False).limit(10)
    return render_template('web2_filter.html', top10_service2=top10_service2)


@app.route('/customer')
def customer():
    all_service2 = Service2.objects()
    return render_template('web2_customer.html', all_service2 = all_service2)


if __name__ == '__main__':
    app.run(debug=True)
 