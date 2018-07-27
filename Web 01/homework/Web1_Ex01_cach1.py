from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>/')
def bmi(weight,height):
    bmi_result = weight/height/height*10000
    if bmi_result < 16:
        result = "Severely underweight"
    elif 16 <= bmi_result < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi_result < 25:
        result = "Normal"
    elif 25 <= bmi_result < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return "Your BMI result is {0} and you are {1}".format(bmi_result, result)

if __name__ == '__main__':
  app.run(debug=True)
 