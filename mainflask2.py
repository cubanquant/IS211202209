from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('grades.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return redirect(url_for("showstudents"))


@app.route('/showstudents')
def showstudents():
    conn = get_db_connection()
    students = conn.execute('SELECT student_id, first, last from Students')

    return render_template('showstudents.html', students=students)


@app.route("/searchstudent", methods=['POST', 'GET'])
def search_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        conn = get_db_connection()
        students = conn.execute('SELECT student_id, first, last from Students where student_id = ?', (student_id,))
        return render_template('showstudents.html', students=students)

    return render_template("searchstudent.html")


if __name__ == "__main__":
    app.run(debug=True)
