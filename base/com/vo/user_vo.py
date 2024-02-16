from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.state_vo import StateVO


class UserVO(db.Model):
    __tablename__ = 'user_table'

    user_id = db.Column('user_id', db.Integer, primary_key=True,
                        autoincrement=True)
    user_firstname = db.Column('user_firstname', db.String(100),
                               nullable=False)
    user_lastname = db.Column('user_lastname', db.String(100), nullable=False)
    user_gender = db.Column('user_gender', db.String(100), nullable=False)
    user_address = db.Column('user_address', db.String(100), nullable=False)
    user_contact = db.Column('user_contact', db.String(100), nullable=False)
    user_state_id = db.Column('user_state_id', db.Integer,
                              db.ForeignKey(StateVO.state_id,
                                            ondelete='CASCADE',
                                            onupdate='CASCADE'))
    user_city_id = db.Column('user_city_id', db.Integer,
                             db.ForeignKey(CityVO.city_id, ondelete='CASCADE',
                                           onupdate='CASCADE'))
    user_login_id = db.Column('user_login_id', db.Integer,
                              db.ForeignKey(LoginVO.login_id,
                                            ondelete='CASCADE',
                                            onupdate='CASCADE'))

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_firstname': self.user_firstname,
            'user_lastname': self.user_lastname,
            'user_gender': self.user_gender,
            'user_address': self.user_address,
            'user_contact': self.user_contact,
            'user_state_id': self.user_state_id,
            'user_city_id': self.user_city_id,
            'user_login_id': self.user_login_id
        }


print("--------hey my name is print")

db.create_all()
