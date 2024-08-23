from flask import Flask, render_template, request, redirect
import db
import api

apio = api.API()
dbo = db.Database()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert_data(name, email, password)

    if response:
        return render_template('login.html', message="Registration successful... You can login now!")
    else:
        return render_template('register.html', message="User already exists!")
    
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.verify_login(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Login failed... Please try again!')
    
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')

    result = apio.NER(text)

    return render_template('ner.html', result=result)

@app.route('/Sentiment_Analysis')
def Sentiment_Analysis():
    return render_template('Sentiment_Analysis.html')

@app.route('/perform_Sentiment_Analysis', methods=['post'])
def perform_Sentiment_Analysis():
    text = request.form.get('Sentiment_Analysis_text')

    result = apio.Sentiment_Analysis(text)
    
    return render_template('Sentiment_Analysis.html', result=result)

@app.route('/Language_Detection')
def Language_Detection():
    return render_template('Language_Detection.html')

@app.route('/perform_Language_Detection', methods=['post'])
def perform_Language_Detection():
    text = request.form.get('Language_Detection_text')

    result = apio.Language_Detection(text)
    
    return render_template('Language_Detection.html', result=result)

app.run(debug=True)
