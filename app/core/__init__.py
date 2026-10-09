from flask import Flask

def create_app():
    app = Flask(__name__)

    from core.start_view import start_page
    app.add_url_rule("/", view_func=start_page)

    return app