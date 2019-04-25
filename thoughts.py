from flask import Flask
from flask import render_template, request
from dbconnect import fetch_thoughts, submit_thoughts_db

thoughtsapp = Flask(__name__)

@thoughtsapp.route('/thought_for_the_day1')
def display_thoughts1():
    result = fetch_thoughts()
    result1 = result[0][0].decode()
    print(result1)
    return render_template('index.html', thought_result=result1)

@thoughtsapp.route('/', methods=['POST'])
def submit_thoughts():
    thought = request.form['user_thoughts']
    submit_thoughts_db(thought)
    return "Thought entered successfully!!"


