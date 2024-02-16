from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO
from base.com.vo.transporttype_vo import TransporttypeVO


class TransportDetailVO(db.Model):
    __tablename__ = 'transport_detail_table'
    transport_detail_id = db.Column('transport_detail_id', db.Integer,
                                    primary_key=True, autoincrement=True)
    transport_detail_description = db.Column('transport_detail_description',
                                             db.String(255), nullable=False)
    transport_detail_transport_type_id = db.Column(
        'transport_detail_transport_type_id', db.Integer,
        db.ForeignKey(TransporttypeVO.transporttype_id, ondelete='CASCADE',
                      onupdate='CASCADE'))
    transport_detail_state_id = db.Column('transport_detail_state_id',
                                          db.Integer,
                                          db.ForeignKey(StateVO.state_id,
                                                        ondelete='CASCADE',
                                                        onupdate='CASCADE'))
    transport_detail_city_id = db.Column('transport_detail_city_id',
                                         db.Integer,
                                         db.ForeignKey(CityVO.city_id,
                                                       ondelete='CASCADE',
                                                       onupdate='CASCADE'))
    transport_detail_agency_id = db.Column('transport_detail_agency_id',
                                           db.Integer,
                                           db.ForeignKey(AgencyVO.agency_id,
                                                         ondelete='CASCADE',
                                                         onupdate='CASCADE'))

    def as_dict(self):
        return {
            'transport_detail_id': self.transport_detail_id,
            'transport_detail_transport_type_id': self.transport_detail_transport_type_id,
            'transport_detail_description': self.transport_detail_description,
            'transport_detail_state_id': self.transport_detail_state_id,
            'transport_detail_city_id': self.transport_detail_city_id,
            'transport_detail_agency_id': self.transport_detail_agency_id
        }


db.create_all()
