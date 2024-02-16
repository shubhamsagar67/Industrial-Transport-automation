from flask import request, render_template, redirect

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.transporttype_dao import TransporttypeDAO
from base.com.vo.transporttype_vo import TransporttypeVO


@app.route('/admin/load_transporttype', methods=['GET'])
def admin_load_transporttype():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/addTransporttype.html')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_load_transporttype route exception occured", ex)


@app.route('/admin/add_transporttype', methods=['POST'])
def admin_insert_transporttype():
    try:
        if admin_login_session() == "admin":

            transporttype_name = request.form.get('transporttypeName')
            transporttype_description = request.form.get(
                'transporttypeDescription')
            print(transporttype_name, transporttype_description)

            transporttype_vo = TransporttypeVO()
            transporttype_dao = TransporttypeDAO()

            transporttype_vo.transporttype_name = transporttype_name
            transporttype_vo.transporttype_description = transporttype_description
            transporttype_dao.insert_transporttype(transporttype_vo)

            return redirect('/admin/view_transporttype')
        else:
            admin_logout_session()

    except Exception as ex:
        print("admin_insert_transporttype route exception occured", ex)


@app.route('/admin/view_transporttype', methods=['GET'])
def admin_view_transporttype():
    try:
        if admin_login_session() == "admin":

            transporttype_dao = TransporttypeDAO()
            transporttype_vo_list = transporttype_dao.view_transporttype()
            print("in admin_view_transporttype transporttype_vo_list",
                  transporttype_vo_list)
            return render_template('admin/viewTransporttype.html',
                                   transporttype_vo_list=transporttype_vo_list)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_view_transporttype route exception occured", ex)


@app.route('/admin/delete_transporttype', methods=['GET'])
def admin_delete_tansporttype():
    try:
        if admin_login_session() == "admin":

            transporttype_vo = TransporttypeVO()
            transporttype_dao = TransporttypeDAO()

            transporttype_id = request.args.get('transporttype_id')

            transporttype_vo.transporttype_id = transporttype_id

            transporttype_dao.delete_transporttype(transporttype_vo)
            return redirect('/admin/view_transporttype')
            print("admin_delete_tansporttype", transporttype_id)

        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_delete_transporttype route exception occured", ex)


@app.route('/admin/edit_transporttype', methods=['GET'])
def admin_edit_transporttype():
    try:
        if admin_login_session() == "admin":

            transporttype_vo = TransporttypeVO()
            transporttype_dao = TransporttypeDAO()

            transporttype_id = request.args.get('transporttype_id')

            transporttype_vo.transporttype_id = transporttype_id

            transporttype_vo_list = transporttype_dao.edit_transporttype(
                transporttype_vo)
            return render_template('admin/editTransporttype.html',
                                   transporttype_vo_list=transporttype_vo_list)
        else:
            admin_logout_session()

    except Exception as ex:
        print("admin_edit_transporttype route exception occured", ex)


@app.route('/admin/update_transporttype', methods=['POST'])
def admin_update_transporttype():
    try:
        if admin_login_session() == "admin":

            transporttype_id = request.form.get('transporttypeId')
            transporttype_name = request.form.get('transporttypeName')
            transporttype_description = request.form.get(
                'transporttypeDescription')

            transporttype_vo = TransporttypeVO()
            transporttype_dao = TransporttypeDAO()

            transporttype_vo.transporttype_id = transporttype_id
            transporttype_vo.transporttype_name = transporttype_name
            transporttype_vo.transporttype_description = transporttype_description

            transporttype_dao.update_transporttype(transporttype_vo)

            return redirect('/admin/view_transporttype')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_update_transporttype route exception occured", ex)
