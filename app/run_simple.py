from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<h1>Hallo von Flask</h1>"

if __name__ == "__main__":
    app.run(debug=True)