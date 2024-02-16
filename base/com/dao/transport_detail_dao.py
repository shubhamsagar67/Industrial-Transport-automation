from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO
from base.com.vo.transport_detail_vo import TransportDetailVO
from base.com.vo.transporttype_vo import TransporttypeVO


class TransportDetailDAO:
    def insert_transport_details(self, transport_detail_vo):
        db.session.add(transport_detail_vo)
        db.session.commit()

    def view_transport_details(self):
        transport_details_vo_list = db.session.query(TransporttypeVO, StateVO,
                                                     CityVO, AgencyVO,
                                                     TransportDetailVO).filter(
            TransporttypeVO.transporttype_id == TransportDetailVO.transport_detail_transport_type_id).filter(
            StateVO.state_id == TransportDetailVO.transport_detail_state_id).filter(
            CityVO.city_id == TransportDetailVO.transport_detail_city_id).filter(
            AgencyVO.agency_id == TransportDetailVO.transport_detail_agency_id).all()
        return transport_details_vo_list

    def delete_transport_details(self, transport_detail_vo):
        transport_details_vo_list = TransportDetailVO.query.get(
            transport_detail_vo.transport_detail_id)
        db.session.delete(transport_details_vo_list)
        db.session.commit()

    def edit_transport_details(self, transport_detail_vo):
        transport_details_vo_list = TransportDetailVO.query.filter_by(
            transport_detail_id=transport_detail_vo.transport_detail_id).all()
        return transport_details_vo_list

    def update_transport_details(self, transport_detail_vo):
        db.session.merge(transport_detail_vo)
        db.session.commit()