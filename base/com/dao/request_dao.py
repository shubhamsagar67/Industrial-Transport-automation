from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.request_vo import RequestVO
from base.com.vo.state_vo import StateVO
from base.com.vo.transporttype_vo import TransporttypeVO


class RequestDAO:
    def insert_request(self, request_vo):
        db.session.add(request_vo)
        db.session.commit()

    def agency_view_request(self, request_vo):
        request_vo_source_list = db.session.query(RequestVO, StateVO, CityVO,
                                                  TransporttypeVO, LoginVO) \
            .filter_by(request_agency_id=request_vo.request_agency_id) \
            .filter(StateVO.state_id == RequestVO.request_source_state_id) \
            .filter(LoginVO.login_id == RequestVO.request_login_id) \
            .filter(CityVO.city_id == RequestVO.request_source_city_id) \
            .filter(
            TransporttypeVO.transporttype_id == RequestVO.request_transporttype_id) \
            .all()
        print("request_vo_source_list=", request_vo_source_list)
        request_vo_destination_list = db.session.query(RequestVO, StateVO,
                                                       CityVO, TransporttypeVO,
                                                       LoginVO) \
            .filter_by(request_agency_id=request_vo.request_agency_id) \
            .filter(StateVO.state_id == RequestVO.request_destination_state_id) \
            .filter(LoginVO.login_id == RequestVO.request_login_id) \
            .filter(CityVO.city_id == RequestVO.request_destination_city_id) \
            .filter(
            TransporttypeVO.transporttype_id == RequestVO.request_transporttype_id) \
            .all()
        print("request_vo_destination_list=", request_vo_destination_list)
        return request_vo_source_list, request_vo_destination_list

    def update_request(self, request_vo):
        request_vo_list = db.session.merge(request_vo)
        db.session.commit()
        print("request_vo_list=", request_vo_list)
        return request_vo_list
