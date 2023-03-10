from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", arr=['kang','odin','galactus'])

@app.route("/<name>")
def test(name):
    return render_template("name.html", content=name)

if __name__ == "__main__":
    app.run()