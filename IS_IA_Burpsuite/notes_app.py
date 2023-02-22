from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from cryptINS import encryption, decryption
import os
import requests
basedir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(basedir, 'Data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
session2 = requests.Session()
session2.proxies = { 'http': 'http://127.0.0.1:8081'}

class Users(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password



@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # session2.get('http://127.0.0.1:5000/login')
    if request.method == 'POST':
        email_id = request.form['email']
        password1 = request.form['password']
        check_email = Users.query.filter_by(email=email_id).first()
        decrypt_password = decryption(check_email.password)  
        decrypt_password = decrypt_password.decode()  
        if check_email is not None and decrypt_password == password1:
            data = {'data': email_id, 'password': check_email.password}
            # session['email'] = email_id
            success = 'Login SUCCESSFUL'
            # r = session2.post('http://127.0.0.1:5000/notes', data=data)
            requests.post('http://127.0.0.1:5000/notes', data=data)
            r = session2.post('http://127.0.0.1:5000/notes', data=data)
            print(data)
            print(r.text)
            return redirect('notes')
        elif check_email is None:
            error = 'Account Doesn\'t Exists'
            return render_template('Login.html', error=error)
        else:
            error = 'Incorrect Login Credentials'
            return render_template('Login.html', error=error)
    else:
        return render_template('Login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email_id = request.form['email']
        password1 = request.form['password']
        password_copy = request.form['cpassword']
        check_email = Users.query.filter_by(email=email_id).first()
        if check_email is None and password_copy == password1 and len(password1) > 8:
            # session['email'] = email_id
            encrypt_password = encryption(password1)
            new_user = Users(email=email_id, password=encrypt_password)
            data = {'data': email_id, 'password': encrypt_password}
            r = session2.post('http://127.0.0.1:5000/login', data=data)
            db.session.add(new_user)
            db.session.commit()
            return redirect('login')
            # return render_template('Login.html', signup=True, data=data)
        elif check_email is not None:
            error = 'Account Already Exists'
            return render_template('SignUp.html', error=error)
        else:
            error = 'Error: Incorrect Password'
            return render_template('SignUp.html', error=error)

    else:
        return render_template('SignUp.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    return render_template('notes.html')


if __name__ == '__main__':
    app.run(port=5000)



