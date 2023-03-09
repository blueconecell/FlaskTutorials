from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>hello!</h1>"

@app.route("/<name>") #꺽쇠 안에 적힌 것이 내용 주소로 적용됨
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for(("home")))

if __name__ == "__main__":
    app.run()