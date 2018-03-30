from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/welcome", methods = ['POST'])
def validate_form():
    user_name = request.form["user_name"]
    pass_word = request.form["pass_word"]
    verify_word = request.form["verify_word"]
    e_mail = request.form["e_mail"]

    user_error = ''
    pw_error = ''
    ver_error = ''
    em_error = ''

    if user_name == '' or len(user_name) > 20 or len(user_name) < 3 or len(user_name.split()) > 1:
        user_error = 'Please enter a valid username'
        user_name =''
        

    if pass_word == '' or len(pass_word) > 30 or len(pass_word) < 3 or len(pass_word.split()) > 1:
        pw_error = 'Please enter a valid password'
        pass_word = ''
        verify_word = ''
    
    if verify_word != pass_word :
        ver_error = 'Make sure the passwords match'
        pass_word = ''
        verify_word = ''

    if e_mail != '':
        if len(e_mail) > 30 or len(e_mail) < 3 or len(e_mail.split()) > 1 or '@' not in e_mail or '.' not in e_mail:
           em_error = 'Please enter a valid email address'
           pass_word = ''
           verify_word = ''
           e_mail = ''

    if not user_error and not pw_error and not ver_error and not em_error:
        return render_template('welcome.html', user_name = user_name)
    else:
        return render_template('edit.html', user_name = user_name , user_error = user_error, pass_word = '',
        pw_error = pw_error, verify_word = '', ver_error = ver_error, e_mail = e_mail, em_error = em_error)

    
@app.route("/signup")
def index():
    return render_template('edit.html')


app.run()