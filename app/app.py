# import os
# from functools import wraps

from flask import Flask, render_template, session, redirect, send_from_directory

app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')


# Database
# mongo_host = os.environ.get('MONGODB_HOST')
# mongo_port = int(os.environ.get('MONGODB_PORT'))
#
# client = pymongo.MongoClient(mongo_host, mongo_port)
# db = client.twinpeaks


# Routes
# from user import routes


# Decorator
# def login_required(f):
#      @wraps(f)
#      def wrap(*arg, **kwargs):
#          if 'logged_in' in session:
#              return f(*arg, **kwargs)
#          else:
#              return redirect('/')
#
#      return wrap


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
def index():
    return 'Hello, World!'


# @app.route('/login')
# def home():
#     if 'logged_in' in session:
#         return redirect('/')
#     return render_template('login.html')
#
#
# @app.route('/register')
# def reg():
#     if 'logged_in' in session:
#         return redirect('/')
#     return render_template('reg.html')
#
# @app.route('/video/<string:file_name>')
# def stream(file_name):
#     video_dir = '../movies'
#     return send_from_directory(directory=video_dir, filename=file_name)


if __name__ == '__main__':
    app.run()
