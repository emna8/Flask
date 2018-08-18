from flask import Flask, render_template

# this is an example of flask app

app = Flask(__name__)


@app.route("/")
def index():
    x = "Emna"
    return render_template("index.html", my_name=x)


if __name__ == '__main__':
    app.run(debug=True)
