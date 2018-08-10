from flask import *
from models.service import Service
import mlab
from models.user import User
from models.order import Order
import datetime

app = Flask(__name__)

mlab.connect()
#mongoengine

app.secret_key = 'a super secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customerlist')
def customerlist():
    all_service = Service.objects()
    return render_template('web3_ex02.html', all_service=all_service)

@app.route('/search-more')
def searchmore():    
    all_service = Service.objects(status=False)
    return render_template('web3_ex03_searchmore.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    id_to_view = service_id
    id = Service.objects.get(id=id_to_view)
    session['service_id'] = service_id
    if 'logged_in' in session:
        if id is not None:
            return render_template('web3_ex03_detail.html', id=id)
        else:
            print("Not found")
    else:
        return redirect (url_for('login'))


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


@app.route('/sign-in', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('web4_signin.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form ['password']
        fullname = form['fullname']
        email = form['email']

        if email.find("@") > 0 and email.find(".") > 0:
            check_username =  User.objects.filter(username=username).first()
            if check_username:
                return "Username đã tồn tại trên hệ thống"
            else:
                new_user = User(
                    username = username,
                    password = password,
                    email = email,
                    fullname = fullname,
                )

                new_user.save()

                session ['logged_in'] = True
                return redirect (url_for('admin'))
        else:
            return "Vui lòng nhập đúng định dạng email"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('web4_login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form ['password']

        userlogin = User.objects.filter(username=username, password=password).first()
        if userlogin:
            session ['logged_in'] = True
            session ['user_id'] = str(userlogin.id)
            
            if 'service_id' in session:    
                return redirect (url_for('detail',service_id = session ['service_id']))
            else: 
                return redirect (url_for('searchmore'))
        else:
            return render_template('web4_login_wrong.html')


@app.route('/logout')
def logout():
    del session['logged_in']
    return "Bạn đã thoát đăng nhập thành công"


@app.route('/order/')
def order():
    new_order = Order(
        service_id = session['service_id'],
        user_id = session['user_id'],
        time = datetime.datetime.now(),
        is_accept = False
    )
    new_order.save()
    return "Đã yêu cầu dịch vụ"


@app.route('/accept')
def accept():
    all_order = Order.objects(is_accept=False)
    return render_template('web4_accept.html', all_order=all_order)


@app.route('/approve/<service_id>')
def approve(service_id):
    
    id = service_id

    order_update = Order.objects.get(service_id=service_id)
    order_update.update(set__is_accept = True)

    service_update = Service.objects().with_id(id)
    service_update.update(set__status = True)
    
    email(service_update.email)

    return "Da phe duyet"


if __name__ == '__main__':
    app.run(debug=True)
 