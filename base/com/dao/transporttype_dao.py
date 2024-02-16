from base import db
from base.com.vo.transporttype_vo import TransporttypeVO


class TransporttypeDAO:
    def insert_transporttype(self, transporttype_vo):
        db.session.add(transporttype_vo)
        db.session.commit()

    def view_transporttype(self):
        transporttype_vo_list = TransporttypeVO.query.all()
        return transporttype_vo_list

    def delete_transporttype(self, transporttype_vo):
        transporttype_vo_list = TransporttypeVO.query.get(
            transporttype_vo.transporttype_id)
        db.session.delete(transporttype_vo_list)
        db.session.commit()

    def edit_transporttype(self, transporttype_vo):
        transporttype_vo_list = TransporttypeVO.query.filter_by(
            transporttype_id=transporttype_vo.transporttype_id)
        return transporttype_vo_list

    def update_transporttype(self, transporttype_vo):
        db.session.merge(transporttype_vo)
        db.session.commit()
