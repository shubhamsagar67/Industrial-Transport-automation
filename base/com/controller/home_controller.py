from flask import render_template

from base import app
from base.com.dao.user_dao import UserDAO


@app.route('/admin/view_user')
def view_user():
    user_dao = UserDAO()
    user_data = user_dao.view_user()
    print("user_data", user_data)
    return render_template('admin/viewUser.html', data=user_data)


@app.route('/user/complain')
def complain():
    return render_template('user/addComplain.html')


@app.route('/user/feedback')
def feedback():
    return render_template('user/addFeedback.html')


@app.route('/user/register')
def register():
    return render_template('user/addUser.html')


@app.route('/user/login')
def login():
    return render_template('user/login.html')
