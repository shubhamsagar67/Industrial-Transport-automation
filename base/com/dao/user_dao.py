from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.state_vo import StateVO
from base.com.vo.user_vo import UserVO


class UserDAO:
    def insert_user(self, user_vo):
        db.session.add(user_vo)
        db.session.commit()

    def view_user(self):
        user_vo_list = db.session.query(UserVO, CityVO, StateVO,
                                        LoginVO).filter(
            CityVO.city_id == UserVO.user_city_id).filter(
            UserVO.user_state_id == StateVO.state_id).filter(
            UserVO.user_login_id == LoginVO.login_id
        ).all()
        # for user in user_vo_list:
        #     user_city_id_1=CityVO.query.filter_by(city_id=user.user_city_id).first().city_name
        print("uaer", user_vo_list)
        return user_vo_list
