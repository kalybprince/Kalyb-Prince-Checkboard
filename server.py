from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=8, y=8)

@app.route('/<int:x>')
def x_only(x):
    return render_template('index.html', x=x, y=8)

@app.route('/<int:x>/<int:y>')
def x_and_y(x, y):
    return render_template('index.html', x=x, y=y)

@app.errorhandler(404)
def my_error(err_no):
    return f"Sorry! No response.  Try again. ({err_no})"

if __name__=="__main__":
    app.run(debug=True)