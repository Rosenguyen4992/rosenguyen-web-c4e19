from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>/')
def bmical(weight, height):
    bmi_result = weight/height/height*10000
    return render_template('bmical.html', weight = weight, height = height, bmi_result = bmi_result)

if __name__ == '__main__':
  app.run(debug=True)
 