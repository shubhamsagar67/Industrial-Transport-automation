from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.state_vo import StateVO
from base.com.vo.transporttype_vo import TransporttypeVO


class RequestVO(db.Model):
    __tablename__ = "request_table"
    request_id = db.Column("request_id", db.Integer, primary_key=True,
                           autoincrement=True)
    request_source_state_id = db.Column("request_source_state_id", db.Integer,
                                        db.ForeignKey(StateVO.state_id,
                                                      ondelete='CASCADE',
                                                      onupdate='CASCADE'))
    request_source_city_id = db.Column("request_source_city_id", db.Integer,
                                       db.ForeignKey(CityVO.city_id,
                                                     ondelete='CASCADE',
                                                     onupdate='CASCADE'))
    request_transporttype_id = db.Column("request_transporttype_id",
                                         db.Integer,
                                         db.ForeignKey(
                                             TransporttypeVO.transporttype_id,
                                             ondelete='CASCADE',
                                             onupdate='CASCADE'))
    request_agency_id = db.Column("request_agency_id", db.Integer,
                                  db.ForeignKey(AgencyVO.agency_id,
                                                ondelete='CASCADE',
                                                onupdate='CASCADE'))
    request_description = db.Column("request_description", db.String(255),
                                    nullable=False)
    request_transportaion_date = db.Column("request_transportaion_date",
                                           db.Date, nullable=False)
    request_destination_state_id = db.Column("request_destination_state_id",
                                             db.Integer,
                                             db.ForeignKey(StateVO.state_id,
                                                           ondelete='CASCADE',
                                                           onupdate='CASCADE'))
    request_destination_city_id = db.Column("request_destination_city_id",
                                            db.Integer,
                                            db.ForeignKey(CityVO.city_id,
                                                          ondelete='CASCADE',
                                                          onupdate='CASCADE'))
    request_weight = db.Column("request_weight", db.Integer, nullable=False)
    request_quantity = db.Column("request_quantity", db.Integer,
                                 nullable=False)
    request_datetime = db.Column("request_datetime", db.DateTime,
                                 nullable=False)
    request_status = db.Column("request_status", db.String(20), nullable=False)
    request_login_id = db.Column("request_login_id", db.Integer,
                                 db.ForeignKey(LoginVO.login_id,
                                               ondelete='CASCADE',
                                               onupdate='CASCADE'))

    def as_di1ct(self):
        return {
            "request_id": self.request_id,
            "request_source_state_id": self.request_source_state_id,
            "request_source_city_id": self.request_source_city_id,
            "request_transporttype_id": self.request_transporttype_id,
            "request_agency_id": self.request_agency_id,
            "request_description": self.request_description,
            "request_date": self.request_date,
            "request_destination_state_id": self.request_destination_state_id,
            "request_destination_city_id": self.request_destination_city_id,
            "request_weight": self.request_weight,
            "request_quantity": self.request_quantity,
            "request_datetime": self.request_datetime,
            "request_login_id": self.request_login_id

        }


db.create_all()
