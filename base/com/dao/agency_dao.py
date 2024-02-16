from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.state_vo import StateVO


class AgencyDAO:
    def insert_agency(self, agency_vo):
        db.session.add(agency_vo)
        db.session.commit()

    def view_agency(self):
        agency_vo_list = (
            db.session.query(StateVO, CityVO, LoginVO, AgencyVO).filter(
                StateVO.state_id == AgencyVO.agency_state_id).filter(
                CityVO.city_id == AgencyVO.agency_city_id).filter(
                LoginVO.login_id == AgencyVO.agency_login_id).all())
        return agency_vo_list

    def find_agency_id(self, agency_vo):
        agency_vo_list = AgencyVO.query.filter_by(
            agency_login_id=agency_vo.agency_login_id).first()
        agency_id = agency_vo_list.agency_id
        print("--------------------->", agency_id)
        return agency_id

    def find_agency_id_by_city_id(self, agency_vo):
        agency_vo_list = db.session.query(AgencyVO) \
            .filter_by(agency_city_id=agency_vo.agency_city_id) \
            .all()
        print("ajax_agency_vo_list", agency_vo_list)
        return agency_vo_list
