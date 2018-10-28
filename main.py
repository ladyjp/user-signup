from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:launchcode@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
     
    return render_template('signup.html',title="Sign Up!")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    #if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if  username == "":
        username_error = 'Please enter Username'
        username = ''
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = 'Please enter Password with at least 3 characters and 20 or less characters'
            username = ''
        
    if  password == "":
        password_error = 'Please enter Password'
        password = ''
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = 'Please enter Password with at least 3 characters and 20 or less characters'
            password = ''

    if  verify == "":
        verify_error = 'Please verify password'
        verify = ''
    else:
        if verify != password:
            verify_error = 'Verified password must match password'
            verify = ''
    
    if "@" and "." in email != True:
        email_error = 'Please enter a valid email address'


    if not username_error and not password_error and not verify_error and not email_error:
        name = username
        return redirect('/welcome?name={0}'.format(name))

    else: 
        return render_template('signup.html', username_error=username_error, 
            password_error=password_error,
            verify_error=verify_error)



@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    name = request.args.get('name')
    return '<h1>Welcome, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run()