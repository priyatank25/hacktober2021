from flask import Flask, render_template

app = Flask(__name__)

data = ["HacktoberFest", "Programming", "Coding", "Open Source"]
# list of items


@app.route('/')
def index():
    return render_template("index.html", data=data)
# basic function to render the Jinja template and providing the data


if __name__ == "__main__":
    app.run(debug=True)
