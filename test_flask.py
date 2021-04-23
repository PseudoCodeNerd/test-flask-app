from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
            <h2 style='color:blue'>comding shomding - flask app served with uwsgi and nginx</h2>
           """

if __name__ == "__main__":
    app.run(host='0.0.0.0')
