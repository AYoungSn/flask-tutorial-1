from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Sungshin!"

@app.route("/hi")
def hello_world2():
    return "Hi, Sungshin2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
