from flask import Flask , render_template
from flask import request
import image
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/select')
def select():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == 'irenegkp@iitk.ac.in' and password == 'irene':
        return render_template("select.html")
    else:
        return render_template("relogin.html")

@app.route('/webcam')
def webcam():
    return image.video()


app.run()