from flask import render_template, request, jsonify, redirect

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.agency_dao import AgencyDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.state_dao import StateDAO
from base.com.dao.transport_detail_dao import TransportDetailDAO
from base.com.dao.transporttype_dao import TransporttypeDAO
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.transport_detail_vo import TransportDetailVO


@app.route('/agency/load_transport_detail')
def agency_load_transportdetails():
    try:
        if admin_login_session() == "agency":
            transporttype_dao = TransporttypeDAO()
            state_dao = StateDAO()

            transporttype_vo_list = transporttype_dao.view_transporttype()
            state_vo_list = state_dao.view_state()

            return render_template('agency/addTransportdetail.html',
                                   transporttype_vo_list=transporttype_vo_list,
                                   state_vo_list=state_vo_list)
        else:
            return admin_login_session()

    except Exception as ex:
        print("in agency_load_trnasport_details route exception occured", ex)


@app.route('/agency/load_city_ajax_transport_detail')
def agency_load_city_ajax_transport_detail():
    try:
        if admin_login_session() == "agency":
            city_dao = CityDAO()
            city_vo = CityVO()
            transport_detail_state_id = request.args.get(
                'transportDetailStateId')
            print("transport_detail_state_id>>>>>>>>>>>>>",
                  transport_detail_state_id)
            city_vo.city_state_id = transport_detail_state_id
            city_vo_list = city_dao.ajax_get_city(city_vo)
            print("city_vo_list>>>>>", city_vo_list)
            ajax_city_vo_list = [i.as_dict() for i in city_vo_list]
            print("ajax_city_vo_list>>>>>>>>>>>>>", ajax_city_vo_list)
            return jsonify(ajax_city_vo_list)
        else:
            return admin_login_session()
    except Exception as ex:
        print("in agency_load_trnasport_details route exception occured", ex)


@app.route('/agency/insert_transport_detail', methods=['POST'])
def agency_insert_transportdetails():
    try:
        if admin_login_session() == "agency":
            transport_detail_transport_type_id = request.form.get(
                'transportDetailTransportTypeId')
            transport_detail_description = request.form.get(
                'transportDetailTransportDescription')
            transport_detail_state_id = request.form.getlist(
                'transportDetailStateId')
            transport_detail_city_id = request.form.getlist(
                'transportDetailCityId')

            transport_detail_state_id.pop(-1)
            transport_detail_city_id.pop(-1)

            login_username = request.cookies.get("login_username")

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            agency_vo = AgencyVO()
            agency_dao = AgencyDAO()

            agency_vo.agency_login_id = login_id
            transport_detail_agency_id = agency_dao.find_agency_id(agency_vo)

            transport_detail_dao = TransportDetailDAO()

            for i in range(len(transport_detail_state_id)):
                transport_detail_vo = TransportDetailVO()
                transport_detail_vo.transport_detail_transport_type_id = transport_detail_transport_type_id
                transport_detail_vo.transport_detail_description = transport_detail_description
                transport_detail_vo.transport_detail_state_id = \
                    transport_detail_state_id[i]
                transport_detail_vo.transport_detail_city_id = \
                    transport_detail_city_id[i]
                transport_detail_vo.transport_detail_agency_id = transport_detail_agency_id
                transport_detail_dao.insert_transport_details(
                    transport_detail_vo)

            return redirect('/agency/view_transport_detail')
        else:
            return admin_login_session()

    except Exception as ex:
        print("in agency_insert_trnasport_details route exception occured", ex)


@app.route('/agency/view_transport_detail', methods=['GET'])
def agency_view_transportdetails():
    try:
        if admin_login_session() == "agency":
            transport_detail_dao = TransportDetailDAO()
            transport_details_vo_list = transport_detail_dao.view_transport_details()
            print(transport_details_vo_list)
            return render_template('agency/viewTransportDetails.html',
                                   transport_details_vo_list=transport_details_vo_list)
        else:
            return admin_login_session()

    except Exception as ex:
        print("in agency_view_trnasport_details route exception occured", ex)


@app.route('/agency/delete_transport_detail', methods=['GET'])
def agency_delete_transportdetails():
    try:
        if admin_login_session() == "agency":
            transport_detail_id = request.args.get('transportDetailId')

            transport_detail_vo = TransportDetailVO()
            transport_detail_dao = TransportDetailDAO()

            transport_detail_vo.transport_detail_id = transport_detail_id

            transport_detail_dao.delete_transport_details(transport_detail_vo)
            return redirect('/agency/view_transport_detail')
        else:
            return admin_login_session()

    except Exception as ex:
        print("in agency_delete_trnasport_details route exception occured", ex)


@app.route('/agency/edit_transport_detail', methods=['GET'])
def agency_edit_transportdetails():
    try:
        if admin_login_session() == "agency":
            transporttype_dao = TransporttypeDAO()
            state_dao = StateDAO()

            transporttype_vo_list = transporttype_dao.view_transporttype()
            state_vo_list = state_dao.view_state()

            transport_details_vo = TransportDetailVO()
            transport_details_dao = TransportDetailDAO()

            transport_detail_id = request.args.get('transportDetailId')
            transport_details_vo.transport_detail_id = transport_detail_id

            transport_details_vo_list = transport_details_dao.edit_transport_details(transport_details_vo)

            return render_template("agency/editTransportDetail.html",
                                   transport_details_vo_list=transport_details_vo_list,
                                   transporttype_vo_list=transporttype_vo_list,
                                   state_vo_list=state_vo_list)
        else:
            return admin_login_session()
    except Exception as ex:
        print("in agency_edit_transport_detail route exception occured", ex)


@app.route('/agency/update_transport_detail', methods=['POST'])
def agency_update_transportdetails():
    try:
        if admin_login_session() == "agency":
            transport_detail_id = request.form.get(
                'transportDetailId')
            transport_detail_transport_type_id = request.form.get(
                'transportDetailTransportTypeId')
            transport_detail_description = request.form.get(
                'transportDetailTransportDescription')
            transport_detail_state_id = request.form.get(
                'transportDetailStateId')
            transport_detail_city_id = request.form.get(
                'transportDetailCityId')

            # transport_detail_state_id.pop(-1)
            # transport_detail_city_id.pop(-1)

            login_username = request.cookies.get("login_username")

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            agency_vo = AgencyVO()
            agency_dao = AgencyDAO()

            agency_vo.agency_login_id = login_id
            transport_detail_agency_id = agency_dao.find_agency_id(agency_vo)

            transport_detail_dao = TransportDetailDAO()

            # for i in range(len(transport_detail_state_id)):
            transport_detail_vo = TransportDetailVO()
            transport_detail_vo.transport_detail_id = transport_detail_id
            transport_detail_vo.transport_detail_transport_type_id = transport_detail_transport_type_id
            transport_detail_vo.transport_detail_description = transport_detail_description
            transport_detail_vo.transport_detail_state_id = \
                transport_detail_state_id
            transport_detail_vo.transport_detail_city_id = \
                transport_detail_city_id
            transport_detail_vo.transport_detail_agency_id = transport_detail_agency_id
            print(transport_detail_vo.__dict__)
            transport_detail_dao.update_transport_details(
                transport_detail_vo)

            return redirect('/agency/view_transport_detail')
        else:
            return admin_login_session()

    except Exception as ex:
        print("in agency_update_trnasport_details route exception occured", ex)
