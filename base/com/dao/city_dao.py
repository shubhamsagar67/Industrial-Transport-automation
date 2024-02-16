from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO


class CityDAO:
    def insert_city(self, city_vo):
        db.session.add(city_vo)
        db.session.commit()

    def view_city(self):
        city_vo_list = db.session.query(CityVO, StateVO) \
            .join(StateVO, CityVO.city_state_id == StateVO.state_id) \
            .all()
        return city_vo_list

    def delete_city(self, city_id):
        city_vo_list = CityVO.query.get(city_id)
        db.session.delete(city_vo_list)
        db.session.commit()

    def edit_city(self, city_vo):
        city_vo_list = CityVO.query.filter_by(city_id=city_vo.city_id).all()
        return city_vo_list

    def update_city(self, city_vo):
        db.session.merge(city_vo)
        db.session.commit()

    def ajax_get_city(self, city_vo):
        city_vo_list = CityVO.query.filter_by(
            city_state_id=city_vo.city_state_id).all()
        return city_vo_list
