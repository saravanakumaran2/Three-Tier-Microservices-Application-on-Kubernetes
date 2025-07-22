from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5001"

@app.route('/')
def home():
    return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        res = requests.post(f"{BACKEND_URL}/login", json=request.form)
        if res.status_code == 200:
            return render_template("main.html", username=request.form['username'])
        return "Login Failed", 401
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        res = requests.post(f"{BACKEND_URL}/register", json=request.form)
        if res.status_code == 201:
            return redirect('/login')
        return "Register Failed", 400
    return render_template("register.html")
