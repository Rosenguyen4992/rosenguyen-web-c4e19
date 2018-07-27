from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def profile(username):
    profile = [
        {
            "username": "nhungnhuc",
            "name": "NHUNG THỊ NHÚC",
            "image": "https://image.ibb.co/k9sqyo/2.jpg",
            "nhandang": "Xinh gái, dam dang, sở thích hay thả thính",
        },
        {
            "username": "tuananh",
            "name": "Tứng Anh",
            "image": "https://image.ibb.co/efppPT/1.jpg",
            "nhandang": "Đẹp trai, thông minh mỗi tội hay bốc phét",
        },
        {
            "username": "anhquan",
            "name": "Anh Quân",
            "image": "https://preview.ibb.co/kvaPr8/3.jpg",
            "nhandang": "Thanh niên nghiêm túc thế hệ 4.0, yêu màu hồng, ghét sự yếu đuối, nhân vật yêu thích Maria Ozawa",
        }
    ]

    for i in range (3):
        if username == profile[i]['username']:
            return render_template('profile.html', profile = profile[i])
    return "Sorry user not found"

if __name__ == '__main__':
  app.run(debug=True)
 