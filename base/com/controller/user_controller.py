import random
import string

from flask import render_template, request, flash, redirect, jsonify

from base import app
from base.com.dao.city_dao import CityDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.state_dao import StateDAO
from base.com.dao.user_dao import UserDAO
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import UserVO


@app.route('/user/load_user', methods=['GET'])
def admin_load_user():
    try:

        state_dao = StateDAO()

        state_vo_list = state_dao.view_state()

        return render_template('user/addUser.html',
                               state_vo_list=state_vo_list)
    except Exception as ex:
        print("in user_load_user route exception occured>>>>>>>>>>", ex)


@app.route('/user/load_city_ajax_user_detail')
def user_load_city_ajax_user_detail():
    try:
        city_dao = CityDAO()
        city_vo = CityVO()
        user_state_id = request.args.get('userStateId')
        print("transport_detail_state_id>>>>>>>>>>>>>", user_state_id)
        city_vo.city_state_id = user_state_id
        city_vo_list = city_dao.ajax_get_city(city_vo)
        print("city_vo_list>>>>>", city_vo_list)
        ajax_city_vo_list = [i.as_dict() for i in city_vo_list]
        print("ajax_city_vo_list>>>>>>>>>>>>>", ajax_city_vo_list)
        return jsonify(ajax_city_vo_list)

    except Exception as ex:
        print("in load_city_ajax_user_detail route exception occured", ex)


@app.route('/user/insert_user', methods=['POST'])
def admin_insert_user():
    print("--------------------------admin_insert_user-----------------------")
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()

        user_vo = UserVO()
        user_dao = UserDAO()

        login_username = request.form.get('loginUsername')
        login_password = request.form.get('loginUserpassword')
        user_firstname = request.form.get('userFirstname')
        user_lastname = request.form.get('userLastname')
        user_gender = request.form.get('userGender')
        user_address = request.form.get('userAddress')
        user_contact = request.form.get('userContact')
        user_state = request.form.get('userState')
        user_city = request.form.get('userCity')

        login_secretkey = ''.join(
            (random.choice(string.ascii_letters + string.digits)) for x in
            range(32))
        print("in user_insert_user login_secretkey>>>>>>>", login_secretkey)
        login_vo_list = login_dao.view_login()
        print("in user_insert_user login_vo_list>>>>>>", login_vo_list)
        if len(login_vo_list) != 0:
            for i in login_vo_list:
                if i.login_secretkey == login_secretkey:
                    login_secretkey = ''.join(
                        (random.choice(string.ascii_letters + string.digits))
                        for x in range(32))
                elif i.login_username == login_username:
                    error_message = "The username is already exists !"
                    flash(error_message)
                    return redirect('/user/load_user')

        login_vo.login_username = login_username
        login_vo.login_password = login_password
        login_vo.login_role = "user"
        login_vo.login_status = "active"
        login_vo.login_secretkey = login_secretkey
        print("--------------login_vo-------------->", login_vo.__dict__)
        login_dao.insert_login(login_vo)

        user_vo.user_firstname = user_firstname
        print(1, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_lastname = user_lastname
        print(2, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_gender = user_gender
        print(3, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_address = user_address
        print(4, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_contact = int(user_contact)
        print(5, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_state_id = user_state
        print(6, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_city_id = user_city
        print(7, "--------------user_vo-------------->", user_vo.__dict__)
        user_vo.user_login_id = login_vo.login_id
        print(8, "--------------user_vo-------------->", user_vo.__dict__)
        user_dao.insert_user(user_vo)

        return redirect("/")
    except Exception as ex:
        print("in user_insert_user route exception occured>>>>>>>>>>", ex)
