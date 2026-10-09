from flask import render_template

def start_page():
    return render_template("index.html")