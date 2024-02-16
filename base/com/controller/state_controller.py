from flask import request, render_template, redirect

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.state_dao import StateDAO
from base.com.vo.state_vo import StateVO


@app.route('/admin/load_state', methods=['GET'])
def admin_load_state():
    try:
        if admin_login_session() == "admin":

            return render_template('admin/addState.html')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_load_category route exception occured ", ex)


@app.route('/admin/add_state', methods=['POST'])
def admin_insert_state():
    try:
        if admin_login_session() == "admin":

            state_name = request.form.get('stateName')
            state_description = request.form.get('stateDescription')
            print(state_name, state_description)

            state_vo = StateVO()
            state_dao = StateDAO()

            state_vo.state_name = state_name
            state_vo.state_description = state_description
            state_dao.insert_state(state_vo)
            return redirect('/admin/view_state')
        else:
            return admin_login_session()

    except Exception as ex:
        print("admin_insert_state route exception occured ", ex)


@app.route('/admin/view_state', methods=['GET'])
def admin_view_state():
    try:
        if admin_login_session() == "admin":

            state_dao = StateDAO()
            state_vo_list = state_dao.view_state()
            print("in admin_view_state state_vo_list", state_vo_list)
            return render_template('admin/viewState.html',
                                   state_vo_list=state_vo_list)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_view_state route exception occured", ex)


@app.route('/admin/delete_state', methods=['GET'])
def admin_delete_state():
    try:
        if admin_login_session() == "admin":

            state_vo = StateVO()
            state_dao = StateDAO()

            state_id = request.args.get('state_id')

            state_vo.state_id = state_id

            state_dao.delete_state(state_vo)
            return redirect('/admin/view_state')

        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_delete_state route exception occured ", ex)


@app.route('/admin/edit_state', methods=['GET'])
def admin_edit_state():
    try:
        if admin_login_session() == "admin":

            state_vo = StateVO()
            state_dao = StateDAO()

            state_id = request.args.get('state_id')

            state_vo.state_id = state_id

            state_vo_list = state_dao.edit_state(state_vo)
            return render_template('admin/editState.html',
                                   state_vo_list=state_vo_list)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_edit_state route exception occured ", ex)


@app.route('/admin/update_state', methods=['POST'])
def admin_update_state():
    try:
        if admin_login_session() == "admin":

            state_id = request.form.get('stateId')
            state_name = request.form.get('stateName')
            state_description = request.form.get('stateDescription')

            state_vo = StateVO()
            state_dao = StateDAO()

            state_vo.state_id = state_id
            state_vo.state_name = state_name
            state_vo.state_description = state_description

            state_dao.update_state(state_vo)
            return redirect("/admin/view_state")
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_update_state route exception occured ", ex)
