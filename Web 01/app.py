from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title": "Thơ về (.)(.)",
            "content": "Cuộc đời thật lắm bất công/ Thằng 2 (.)(.) thằng 0 (.)(.)",
            "author": "Nhung nhúc",
            "gender": 1
        },
        {
            "title": "Thơ về (.)(.)2",
            "content": "Cuộc đời thật lắm bất công/ Thằng 2 (.)(.) thằng 0 (.)(.)",
            "author": "Nhung nhúc",
            "gender": 1
        },
        {
            "title": "Thơ về (.)(.)3",
            "content": "Cuộc đời thật lắm bất công/ Thằng 2 (.)(.) thằng 0 (.)(.)",
            "author": "Nhung nhúc",
            "gender": 0
        }
    ]
    

    return render_template("tem.html", posts=posts)

# @app.route('/say-hi/<name>/<age>')
# def hello(name, age):
#     return "Hi {0} you are {1} years old".format(name, age)

# @app.route('/sum/<x>/<y>')
# def calsum(x, y):
#     res = int(x) + int(y)
#     return "{0} + {1} = {2}".format(x, y, res)

# @app.route('/sum/<int:x>/<int:y>')
# def calsum(x, y):
#     return str(x+y)

if __name__ == '__main__':
  app.run(debug=True)
 