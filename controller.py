from flask import render_template, request

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    login = request.form.get('userLogin')
    email = request.form.get('userMail')
    psw = request.form.get('userPassword')
    print(login, email, psw)
    return render_template('contacts.html')
