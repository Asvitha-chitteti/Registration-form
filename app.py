from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create table if not exists
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            email TEXT UNIQUE,
            password TEXT,
            phone TEXT,
            dob TEXT,
            gender TEXT,
            address TEXT,
            registered_on TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['address']
        registered_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users 
            (fullname, email, password, phone, dob, gender, address, registered_on)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (fullname, email, password, phone, dob, gender, address, registered_on))
        conn.commit()
        conn.close()

        return render_template("success.html")

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)