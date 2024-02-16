import datetime

from flask import render_template, request, redirect

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.agency_dao import AgencyDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.order_dao import OrderDAO
from base.com.dao.quotation_dao import QuotationDAO
from base.com.dao.request_dao import RequestDAO
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.order_vo import OrderVO
from base.com.vo.quotation_vo import QuotationVO
from base.com.vo.request_vo import RequestVO


@app.route('/agency/insert_quotation', methods=['POST'])
def agency_insert_quotation():
    try:
        if admin_login_session() == 'agency':

            request_id = request.form.get("requestId")
            quotation_price = request.form.get("quotationPrice")
            quotation_delivery_duration = request.form.get("deliveryDuration")
            quotation_comment = request.form.get("quotationComment")

            request_vo = RequestVO()
            request_dao = RequestDAO()

            request_vo.request_id = request_id
            request_vo.request_status = "approved"

            request_vo_list = request_dao.update_request(request_vo)

            quotation_vo = QuotationVO()
            quotation_dao = QuotationDAO()

            quotation_vo.quotation_price = quotation_price
            quotation_vo.quotation_comment = quotation_comment
            quotation_vo.quotation_datetime = datetime.datetime.now()
            quotation_vo.quotation_delivery_duration = quotation_delivery_duration
            quotation_vo.quotation_status = "pending"
            quotation_vo.quotation_request_id = request_id

            quotation_dao.insert_quotation(quotation_vo)

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_id = request_vo_list.request_login_id
            login_vo.login_id = login_id
            login_username = login_dao.find_login_username(login_vo)

            return redirect('/agency/view_request')

        else:
            return admin_logout_session()
    except Exception as ex:
        print("in agency_insert_quotation route exception occured>>>>>>>>>>",
              ex)


@app.route('/agency/view_quotation', methods=['GET'])
def agency_view_quotation():
    try:
        if admin_login_session() == 'agency':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')

            login_id = login_dao.find_login_id(login_vo)

            agency_vo = AgencyVO()
            agency_dao = AgencyDAO()

            agency_vo.agency_login_id = login_id
            print("-----------agency_vo-------------->", agency_vo.__dict__)
            agency_id = agency_dao.find_agency_id(agency_vo)

            request_vo = RequestVO()
            print("-----------agency_id-------------->", agency_id)
            request_vo.request_agency_id = agency_id

            quotation_dao = QuotationDAO()

            quotation_vo_list = quotation_dao.agency_view_quotation(request_vo)
            print("quotation_vo_list", quotation_vo_list)
            return render_template('agency/viewQuotation.html',
                                   quotation_vo_list=quotation_vo_list)

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in agency_view_quotation route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_quotation')
def user_view_quotation():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            request_vo = RequestVO()

            request_vo.request_login_id = login_id

            quotation_dao = QuotationDAO()

            quotation_vo_list = quotation_dao.view_quotation(request_vo)

            return render_template('user/viewQuotation.html',
                                   quotation_vo_list=quotation_vo_list)

        else:
            return admin_logout_session()

    except Exception as ex:
        print("in agency_view_quotation route exception occured>>>>>>>>>>", ex)


@app.route('/user/reject_quotation', methods=['GET'])
def user_reject_quotation():
    try:
        if admin_login_session() == "user":

            quotation_id = request.args.get("quotationId")
            print("quotationId>>>>>", quotation_id)

            quotation_vo = QuotationVO()
            quotation_dao = QuotationDAO()

            quotation_vo.quotation_id = quotation_id
            quotation_vo.quotation_status = "rejected"

            quotation_vo_list = quotation_dao.update_quotation(quotation_vo)

            print("quotation_vo_list=", quotation_vo_list)

            request_vo = RequestVO()
            request_dao = RequestDAO()

            request_vo.request_id = quotation_vo_list.quotation_request_id
            request_vo.request_status = "rejected"

            request_dao.update_request(request_vo)

            return redirect('/user/view_quotation')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_reject_quotation route exception occured>>>>>>>>>>", ex)


@app.route('/user/approve_quotation', methods=['GET'])
def user_approve_quotation():
    try:
        if admin_login_session() == "user":

            quotation_id = request.args.get("quotationId")
            agency_id = request.args.get("agencyId")
            print("quotationId>>>>>", quotation_id, agency_id)

            quotation_vo = QuotationVO()
            quotation_dao = QuotationDAO()

            quotation_vo.quotation_id = quotation_id
            quotation_vo.quotation_status = "approved"

            quotation_vo_list = quotation_dao.update_quotation(quotation_vo)

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            order_vo = OrderVO()
            order_dao = OrderDAO()

            order_vo.order_quotation_id = quotation_id
            order_vo.order_status = "pending"
            order_vo.order_datetime = datetime.datetime.now()
            order_vo.order_login_id = login_id
            order_vo.order_agency_id = agency_id

            order_dao.insert_order(order_vo)

            return redirect('/user/view_quotation')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_approve_quotation route exception occured>>>>>>>>>>", ex)
