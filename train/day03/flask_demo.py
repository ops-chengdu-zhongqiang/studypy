#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年5月5日

@author: zhongqiang

Describe: flask 学习
'''

from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/') #使用 route() 装饰器来告诉 Flask 触发函数的 URL
def hello_world():
    return "Hello World!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

def do_the_login():
    pass

def show_the_login_form():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()








if __name__ == "__main__":
    with app.test_request_context():
        url_for('about')
        url_for('projects')
    app.run("127.0.0.1", 80, debug=True)














