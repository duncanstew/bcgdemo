from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('courses.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/completed')
def completed():
    return render_template('completed.html')

@app.route('/journeys')
def journeys():
    return render_template('journeys.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/course_home')
def course_home():
    return render_template('course_home.html')

@app.route('/community')
def community():
    topics = ['Beecoming an SME', 'Gantt Charts', 'Organization Methods', 'Sprint Retrospective','Sprint Review']
    questions = [
    ('Does anybody have tips on how to transition from Waterfall to Agile as a company?',0,3, 'Unresolved'),
    ('How many Story Points whould we aim for each Sprint?',45,3,'Unresolved'),
    ('Does anybody have tips on how to transition from Waterfall to Agile as a copmany?',45,3,'Unresolved'),
    ('Does anyone know what was said about Gantt charts on Tuesday',200,3,'Unresolved'),
        ('Does anybody have tips on how to transition from Waterfall to Agile as a company?',0,3, 'Unresolved'),
    ('How many Story Points whould we aim for each Sprint?',45,3,'Unresolved'),
    ('Does anybody have tips on how to transition from Waterfall to Agile as a copmany?',45,3,'Unresolved'),
    ('Does anyone know what was said about Gantt charts on Tuesday',200,3,'Unresolved'),
     ]
    return render_template('community.html',topics=topics,questions=questions)

@app.route('/coaching')
def coaching():
    return render_template('coaching.html')


if __name__ == "__main__":
    app.run(debug=True)