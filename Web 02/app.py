from flask import *
from models.service import Service
import mlab

app = Flask(__name__)

mlab.connect()
#mongoengine


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customerlist')
def customerlist():
    all_service = Service.objects()
    return render_template('web3_ex02.html', all_service=all_service)

@app.route('/search-more')
def searchmore():
    all_service = Service.objects()
    return render_template('web3_ex03.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    id_to_view = service_id
    id = Service.objects.get(id=id_to_view)
    if id is not None:
        return render_template('web3_ex03_detail.html', id=id)
    else:
        print("Not found")

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender, yob__lte=1998, address__icontains="Nội")
    return render_template('search.html', all_service = all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    id_to_delete = service_id
    id = Service.objects.get(id=id_to_delete)
    if id is not None:
        id.delete()
        return redirect (url_for('admin'))
    else:
        print("Not found")

@app.route('/update-service/<service_id>', methods = ["GET", "POST"])
def update_service(service_id):
    id_to_update = service_id
    id = Service.objects.get(id=id_to_update)
    if id is not None:
        if request.method == "GET":
            return render_template('web3_ex06_update.html', id = id)
        elif request.method == "POST":
            form = request.form
            id.update (
                set__name = form['name'],
                set__yob = form['yob'],
                set__gender = form['gender'],
                set__phone = form['phone'],
                set__address = form['address'],
                set__height = form['height']  
            )
            return redirect(url_for('admin'))
    else:
        print("Not found")

@app.route('/new-service', methods = ["GET", "POST"])
def new_service():
    if request.method == "GET":
        return render_template('web3_ex04_newservice.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        height = form ['height']
        phone = form ['phone']
        gender = form['gender']
        address = form['address']

        new_service = Service(
            name = name, 
            yob = yob,
            height = height,
            phone = phone,
            gender = gender,
            address = address,
            )
        new_service.save()

        return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
 