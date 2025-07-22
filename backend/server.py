from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (data['username'], data['password']))
    db.commit()
    return '', 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (data['username'], data['password']))
    user = cursor.fetchone()
    if user:
        return '', 200
    return '', 401
