import datetime

from flask import render_template, request, redirect, jsonify

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.agency_dao import AgencyDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.request_dao import RequestDAO
from base.com.dao.state_dao import StateDAO
from base.com.dao.transporttype_dao import TransporttypeDAO
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.request_vo import RequestVO


@app.route('/user/load_request')
def user_load_request():
    try:
        if admin_login_session() == 'user':
            state_dao = StateDAO()
            state_vo_list = state_dao.view_state()
            transporttype_dao = TransporttypeDAO()
            transporttype_vo_list = transporttype_dao.view_transporttype()

            return render_template('user/postRequest.html',
                                   state_vo_list=state_vo_list,
                                   transporttype_vo_list=transporttype_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_load_request route exception occured>>>>>>>>>>", ex)


@app.route('/user/load_agency_detail_ajax', methods=['GET'])
def load_agency_detail_ajax():
    try:
        if admin_login_session() == 'user':
            source_city_id = request.args.get("sourceCityId")
            print("source_city_id", source_city_id)

            agency_vo = AgencyVO()
            agency_dao = AgencyDAO()

            agency_vo.agency_city_id = source_city_id
            agency_vo_list = agency_dao.find_agency_id_by_city_id(agency_vo)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
                  agency_vo_list[0].agency_name)

            ajax_agency_vo_list = [i.as_dict() for i in agency_vo_list]

            print("ajax_agency_vo_list=", ajax_agency_vo_list)

            return jsonify(ajax_agency_vo_list)

        else:
            return admin_logout_session()
    except Exception as ex:
        print("in load_agency_detail_ajax route exception occured>>>>>>>>>>",
              ex)


@app.route('/user/insert_request', methods=['POST'])
def user_insert_request():
    try:
        if admin_login_session() == 'user':

            request_source_state_id = request.form.get("sourceState")
            request_source_city_id = request.form.get("sourceCity")
            request_transporttype_id = request.form.get(
                "requestTransportTypeId")
            request_agency_id = request.form.get("requestAgencyId")
            request_description = request.form.get("requestDescription")
            request_transportaion_date = request.form.get(
                "requestTransportationDate")
            request_destination_state_id = request.form.get("destinationState")
            request_destination_city_id = request.form.get("destinationCity")
            request_weight = request.form.get("requestWeight")
            request_quantity = request.form.get("requestQuantity")
            request_datetime = datetime.datetime.now()

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            request_login_id = login_id

            request_vo = RequestVO()
            request_dao = RequestDAO()

            request_vo.request_source_state_id = request_source_state_id
            request_vo.request_source_city_id = request_source_city_id
            request_vo.request_transporttype_id = request_transporttype_id
            request_vo.request_agency_id = request_agency_id
            request_vo.request_description = request_description
            request_vo.request_transportaion_date = request_transportaion_date
            request_vo.request_destination_state_id = request_destination_state_id
            request_vo.request_destination_city_id = request_destination_city_id
            request_vo.request_weight = request_weight
            request_vo.request_quantity = request_quantity
            request_vo.request_datetime = request_datetime
            request_vo.request_status = "pending"
            request_vo.request_login_id = request_login_id
            request_dao.insert_request(request_vo)

            return redirect('/user/load_request')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_insert_request route exception occured>>>>>>>>>>", ex)


@app.route('/agency/view_request')
def agency_view_request():
    try:
        if admin_login_session() == 'agency':

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            agency_vo = AgencyVO()
            agency_dao = AgencyDAO()

            agency_vo.agency_login_id = login_id
            agency_id = agency_dao.find_agency_id(agency_vo)

            request_vo = RequestVO()
            request_dao = RequestDAO()

            request_vo.request_agency_id = agency_id
            request_vo_source_list, request_vo_destination_list = request_dao.agency_view_request(
                request_vo)
            request_dict_list = []
            for row in range(len(request_vo_source_list)):
                source_dict = {
                    "request_id": request_vo_source_list[row][0].request_id,
                    "login_username": request_vo_source_list[row][
                        4].login_username,
                    "request_datetime": request_vo_source_list[row][
                        0].request_datetime,
                    "request_status": request_vo_source_list[row][
                        0].request_status,
                    "transporttype_name": request_vo_source_list[row][
                        3].transporttype_name,
                    "request_description": request_vo_source_list[row][
                        0].request_description,
                    "source_city_name": request_vo_source_list[row][
                        2].city_name,
                    "source_state_name": request_vo_source_list[row][
                        1].state_name,
                    "destination_city_name": request_vo_destination_list[row][
                        2].city_name,
                    "destination_state_name": request_vo_destination_list[row][
                        1].state_name,
                    "request_login_id": request_vo_source_list[row][
                        0].request_login_id
                }
                request_dict_list.append(source_dict)
            return render_template('agency/viewRequest.html',
                                   request_dict_list=request_dict_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in agency_view_request route exception occured>>>>>>>>>>", ex)


@app.route('/agency/reject_request')
def agency_reject_request():
    try:
        if admin_login_session() == 'agency':

            request_id = request.args.get("requestId")
            request_login_id = request.args.get("requestLoginId")
            print(">>>>>>>>>>", request_login_id)

            request_vo = RequestVO()
            request_dao = RequestDAO()

            request_vo.request_id = request_id
            request_vo.request_status = "rejected"

            request_dao.update_request(request_vo)

            return redirect('/agency/view_request')

        else:
            return admin_logout_session()
    except Exception as ex:
        print("in agency_reject_request route exception occured>>>>>>>>>>", ex)


@app.route('/agency/approve_request')
def agency_approve_request():
    try:
        if admin_login_session() == 'agency':

            request_id = request.args.get("requestId")

            return render_template('agency/addQuotation.html',
                                   request_id=request_id)

        else:
            return admin_logout_session()
    except Exception as ex:
        print("in agency_approve_request route exception occured>>>>>>>>>>",
              ex)
