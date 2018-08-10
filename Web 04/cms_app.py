from flask import *
import mlab
from model.video import Video
from youtube_dl import YoutubeDL

app = Flask(__name__)

app.secret_key = 'a super secret key'

@app.route('/')
def index():
    all_video = Video.objects()
    return render_template('index.html', all_video = all_video)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form ['password']

        if username == 'admin' and password == 'admin':
            session ['logged_in'] = True
            return redirect (url_for('admin'))
        else:
            return "Sai tên đăng nhập hoặc mật khẩu"

@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect (url_for('index'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'logged_in' in session:
        if request.method == 'GET':
            all_video = Video.objects()
            return render_template('admin.html', all_video=all_video)
        elif request.method == 'POST':
            form = request.form
            link = form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)
        
            new_video = Video(
                title = data['title'],
                thumbnail = data['thumbnail'],
                view = data['view_count'],
                youtubeid = data['id']
            )
            new_video.save()
            return redirect(url_for('admin'))
    else:
        return "Đi chỗ khác chơi"

@app.route('/detail/<youtubeid>')
def detail(youtubeid):
    if id is not None:
        return render_template('detail.html', youtubeid=youtubeid)
    else:
        print("Not found")

if __name__ == '__main__':
    app.run(debug=True)
 
