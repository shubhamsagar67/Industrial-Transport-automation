from flask import render_template, request

from base import app
from base.com.controller.login_controller import admin_login_session, \
    admin_logout_session
from base.com.dao.agency_dao import AgencyDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.order_dao import OrderDAO
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.order_vo import OrderVO


# @app.route('/agency/view_order')
# def agency_view_order():
#     try:
#         if admin_login_session() == 'agency':
#             login_vo = LoginVO()
#             login_dao = LoginDAO()
#
#             login_vo.login_username = request.cookies.get('login_username')
#             login_id = login_dao.find_login_id(login_vo)
#
#             agency_vo = AgencyVO()
#             agency_dao = AgencyDAO()
#
#             agency_vo.agency_login_id = login_id
#             agency_id = agency_dao.find_agency_id(agency_vo)
#
#             order_vo = OrderVO()
#             order_dao = OrderDAO()
#
#             order_vo.order_agency_id = agency_id
#             order_vo_list = order_dao.agency_view_order(order_vo)
#             return render_template("agency/viewOrder.html",order_vo_list=order_vo_list)
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("in agency_view_order route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_order')
def user_view_order():
    try:
        if admin_login_session() == 'user':
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            order_vo = OrderVO()
            order_dao = OrderDAO()

            order_vo.order_login_id = login_id
            order_vo_source_list, order_vo_destination_list = order_dao.user_view_order(
                order_vo)
            order_dict_list = []
            for row in range(len(order_vo_source_list)):
                source_dict = {
                    "order_id": order_vo_source_list[row][0].order_id,
                    "login_username": order_vo_source_list[row][
                        1].login_username,
                    "order_agency_name": order_vo_source_list[row][
                        2].agency_name,
                    "order_datetime": order_vo_source_list[row][
                        0].order_datetime,
                    "order_quotation_price": order_vo_source_list[row][
                        3].quotation_price,
                    "order_delivery_duration": order_vo_source_list[row][
                        3].quotation_delivery_duration,
                    "order_transporttype_name": order_vo_source_list[row][
                        5].transporttype_name,
                    "source_city_name": order_vo_source_list[row][6].city_name,
                    "source_state_name": order_vo_source_list[row][
                        7].state_name,
                    "destination_city_name": order_vo_destination_list[row][
                        6].city_name,
                    "destination_state_name": order_vo_destination_list[row][
                        7].state_name
                }
                order_dict_list.append(source_dict)
            print("order_dict_list=", order_dict_list)

            return render_template("user/viewOrder.html",
                                   order_dict_list=order_dict_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_view_order route exception occured>>>>>>>>>>", ex)


@app.route('/agency/view_order')
def agency_view_order():
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

            order_vo = OrderVO()
            order_dao = OrderDAO()

            order_vo.order_agency_id = agency_id
            order_vo_source_list, order_vo_destination_list = order_dao.agency_view_order(
                order_vo)
            order_dict_list = []
            for row in range(len(order_vo_source_list)):
                source_dict = {
                    "order_id": order_vo_source_list[row][0].order_id,
                    "login_username": order_vo_source_list[row][
                        1].login_username,
                    "order_agency_name": order_vo_source_list[row][
                        2].agency_name,
                    "order_datetime": order_vo_source_list[row][
                        0].order_datetime,
                    "order_quotation_price": order_vo_source_list[row][
                        3].quotation_price,
                    "order_delivery_duration": order_vo_source_list[row][
                        3].quotation_delivery_duration,
                    "order_transporttype_name": order_vo_source_list[row][
                        5].transporttype_name,
                    "source_city_name": order_vo_source_list[row][6].city_name,
                    "source_state_name": order_vo_source_list[row][
                        7].state_name,
                    "destination_city_name": order_vo_destination_list[row][
                        6].city_name,
                    "destination_state_name": order_vo_destination_list[row][
                        7].state_name
                }
                order_dict_list.append(source_dict)
            print("order_dict_list=", order_dict_list)

            return render_template("agency/viewOrder.html",
                                   order_dict_list=order_dict_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in agency_view_order route exception occured>>>>>>>>>>", ex)
