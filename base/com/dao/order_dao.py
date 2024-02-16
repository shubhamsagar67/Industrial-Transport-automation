from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.order_vo import OrderVO
from base.com.vo.quotation_vo import QuotationVO
from base.com.vo.request_vo import RequestVO
from base.com.vo.state_vo import StateVO
from base.com.vo.transporttype_vo import TransporttypeVO


class OrderDAO:
    def insert_order(self, order_vo):
        db.session.add(order_vo)
        db.session.commit()

    # def agency_view_order(self, order_vo):
    #     order_vo_list = db.session.query(OrderVO, LoginVO) \
    #         .filter_by(order_agency_id=order_vo.order_agency_id) \
    #         .filter(OrderVO.order_login_id == LoginVO.login_id).all()
    #     print("order_vo_list=", order_vo_list)
    #     return order_vo_list

    def user_view_order(self, order_vo):
        order_vo_source_list = db.session.query(OrderVO, LoginVO, AgencyVO,
                                                QuotationVO, RequestVO,
                                                TransporttypeVO,
                                                CityVO, StateVO) \
            .filter_by(order_login_id=order_vo.order_login_id) \
            .filter(OrderVO.order_login_id == LoginVO.login_id) \
            .filter(OrderVO.order_agency_id == AgencyVO.agency_id) \
            .filter(OrderVO.order_quotation_id == QuotationVO.quotation_id) \
            .filter(RequestVO.request_id == QuotationVO.quotation_request_id) \
            .filter(
            RequestVO.request_transporttype_id == TransporttypeVO.transporttype_id) \
            .filter(RequestVO.request_source_city_id == CityVO.city_id) \
            .filter(RequestVO.request_source_state_id == StateVO.state_id) \
            .all()
        print("order_vo_source_list=", order_vo_source_list)
        order_vo_destination_list = db.session.query(OrderVO, LoginVO,
                                                     AgencyVO, QuotationVO,
                                                     RequestVO,
                                                     TransporttypeVO, CityVO,
                                                     StateVO) \
            .filter_by(order_login_id=order_vo.order_login_id) \
            .filter(OrderVO.order_login_id == LoginVO.login_id) \
            .filter(OrderVO.order_agency_id == AgencyVO.agency_id) \
            .filter(OrderVO.order_quotation_id == QuotationVO.quotation_id) \
            .filter(RequestVO.request_id == QuotationVO.quotation_request_id) \
            .filter(
            RequestVO.request_transporttype_id == TransporttypeVO.transporttype_id) \
            .filter(RequestVO.request_destination_city_id == CityVO.city_id) \
            .filter(RequestVO.request_destination_state_id == StateVO.state_id) \
            .all()
        print("order_vo_destination_list=", order_vo_destination_list)
        return order_vo_source_list, order_vo_destination_list

    def agency_view_order(self, order_vo):
        order_vo_source_list = db.session.query(OrderVO, LoginVO, AgencyVO,
                                                QuotationVO, RequestVO,
                                                TransporttypeVO,
                                                CityVO, StateVO) \
            .filter_by(order_agency_id=order_vo.order_agency_id) \
            .filter(OrderVO.order_login_id == LoginVO.login_id) \
            .filter(OrderVO.order_agency_id == AgencyVO.agency_id) \
            .filter(OrderVO.order_quotation_id == QuotationVO.quotation_id) \
            .filter(RequestVO.request_id == QuotationVO.quotation_request_id) \
            .filter(
            RequestVO.request_transporttype_id == TransporttypeVO.transporttype_id) \
            .filter(RequestVO.request_source_city_id == CityVO.city_id) \
            .filter(RequestVO.request_source_state_id == StateVO.state_id) \
            .all()
        print("order_vo_source_list=", order_vo_source_list)
        order_vo_destination_list = db.session.query(OrderVO, LoginVO,
                                                     AgencyVO, QuotationVO,
                                                     RequestVO,
                                                     TransporttypeVO, CityVO,
                                                     StateVO) \
            .filter_by(order_agency_id=order_vo.order_agency_id) \
            .filter(OrderVO.order_login_id == LoginVO.login_id) \
            .filter(OrderVO.order_agency_id == AgencyVO.agency_id) \
            .filter(OrderVO.order_quotation_id == QuotationVO.quotation_id) \
            .filter(RequestVO.request_id == QuotationVO.quotation_request_id) \
            .filter(
            RequestVO.request_transporttype_id == TransporttypeVO.transporttype_id) \
            .filter(RequestVO.request_destination_city_id == CityVO.city_id) \
            .filter(RequestVO.request_destination_state_id == StateVO.state_id) \
            .all()
        print("order_vo_destination_list=", order_vo_destination_list)
        return order_vo_source_list, order_vo_destination_list
