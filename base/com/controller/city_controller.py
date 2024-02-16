from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.city_dao import CityDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.city_vo import CityVO


@app.route('/admin/load_city', methods=['GET'])
def admin_load_city():
    try:
        if admin_login_session() == "admin":

            state_dao = StateDAO()
            state_vo_list = state_dao.view_state()
            return render_template('admin/addCity.html',
                                   state_vo_list=state_vo_list)

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_load_city route exception occured", ex)


@app.route('/admin/insert_city', methods=['POST'])
def admin_insert_city():
    try:
        if admin_login_session() == "admin":

            city_name = request.form.get('cityName')
            city_description = request.form.get('cityDescription')
            city_state_id = request.form.get('cityStateId')

            city_vo = CityVO()
            city_dao = CityDAO()

            city_vo.city_name = city_name
            city_vo.city_description = city_description
            city_vo.city_state_id = city_state_id

            city_dao.insert_city(city_vo)
            return redirect(url_for('admin_view_city'))

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_insert_city route exception occured", ex)


@app.route('/admin/view_city', methods=['GET'])
def admin_view_city():
    try:
        if admin_login_session() == "admin":

            city_dao = CityDAO()
            city_vo_list = city_dao.view_city()
            # print("city_vo_list", city_vo_list)
            return render_template('admin/viewCity.html',
                                   city_vo_list=city_vo_list)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_view_city route exception occured", ex)


@app.route('/admin/delete_city', methods=['GET'])
def admin_delete_city():
    try:
        if admin_login_session() == "admin":

            city_dao = CityDAO()
            city_id = request.args.get('cityId')

            city_dao.delete_city(city_id)
            return redirect(url_for('admin_view_city'))
        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_delete_city route exception occured", ex)


@app.route('/admin/edit_city', methods=['GET'])
def admin_edit_city():
    try:
        if admin_login_session() == "admin":

            city_vo = CityVO()
            city_dao = CityDAO()
            state_dao = StateDAO()

            city_id = request.args.get('cityId')
            city_vo.city_id = city_id

            city_vo_list = city_dao.edit_city(city_vo)

            state_vo_list = state_dao.view_state()

            return render_template('admin/editCity.html',
                                   state_vo_list=state_vo_list,
                                   city_vo_list=city_vo_list)

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_edit_city route exception occured", ex)


@app.route('/admin/update_city', methods=['POST'])
def admin_update_city():
    try:
        if admin_login_session() == "admin":

            city_id = request.form.get('cityId')
            city_name = request.form.get('cityName')
            city_description = request.form.get('cityDescription')
            city_state_id = request.form.get('cityStateId')

            city_vo = CityVO()
            city_dao = CityDAO()

            city_vo.city_id = city_id
            city_vo.city_name = city_name
            city_vo.city_description = city_description
            city_vo.city_state_id = city_state_id
            print("-----------city_vo---------> ", city_vo.__dict__)
            city_dao.update_city(city_vo)
            return redirect(url_for('admin_view_city'))

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_update_city route exception occured", ex)
