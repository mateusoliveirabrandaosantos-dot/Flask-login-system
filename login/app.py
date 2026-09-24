import pymysql as pms
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
def connection():
    connect = pms.Connection(
        host="localhost",
        user="MOBS",
        password="1029384756Aa.",
        database="logindb",
        charset="utf8mb4",
        cursorclass=pms.cursors.DictCursor,
        port=3306
    )

    return connect

@app.route('/logged')
def logged():
    return render_template('logged.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if password and email and name:
            p_hash = generate_password_hash(password)

            conn = connection()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username, email, hash) VALUES (%s, %s, %s)", (name, email, p_hash))
            cursor.close()
            conn.commit()

            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, hash, username FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user['hash'], password):
            return redirect(url_for('logged'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)