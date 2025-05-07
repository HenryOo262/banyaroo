from flask import Flask
from flask import render_template

def create_app():

    app = Flask(__name__)
    
    @app.route('/')
    def hi():
        return render_template('home.html')

    return app