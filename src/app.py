from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hii, Sungshin!"

@app.route("/hi")
def hello_world2():
    return "Hi, Sungshin2!"

@app.route("/as")
def hello_world():
    return "Hello, Sungshinsdf!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
