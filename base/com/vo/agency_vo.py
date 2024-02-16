from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.state_vo import StateVO


class AgencyVO(db.Model):
    __tablename__ = 'agency_table'

    agency_id = db.Column('agency_id', db.Integer, primary_key=True,
                          autoincrement=True)
    agency_name = db.Column('agency_name', db.String(255), nullable=False)
    agency_contactperson = db.Column('agency_contactperson', db.String(255),
                                     nullable=False)
    agency_registerdate = db.Column('agency_registerdate', db.String(255),
                                    nullable=False)

    agency_certificate_filename = db.Column('agency_certificate_filename',
                                            db.String(255), nullable=False)
    agency_certificate_filepath = db.Column('agency_certificate_filepath',
                                            db.String(255), nullable=False)

    agency_contact = db.Column('agency_contact', db.String(255),
                               nullable=False)
    agency_address = db.Column('agency_address', db.String(255),
                               nullable=False)
    agency_state_id = db.Column('agency_state_id', db.Integer,
                                db.ForeignKey(StateVO.state_id,
                                              ondelete='CASCADE',
                                              onupdate='CASCADE'))
    agency_city_id = db.Column('agency_city_id', db.Integer,
                               db.ForeignKey(CityVO.city_id,
                                             ondelete='CASCADE',
                                             onupdate='CASCADE'))
    agency_login_id = db.Column('agency_login_id', db.Integer,
                                db.ForeignKey(LoginVO.login_id,
                                              ondelete='CASCADE',
                                              onupdate='CASCADE'))

    def as_dict(self):
        return {
            'agency_id': self.agency_id,
            'agency_name': self.agency_name,
            'agency_contactperson': self.agency_contactperson,
            'agency_address': self.agency_address,
            'agency_certificate_filename': self.agency_certificate_filename,
            'agency_certificate_filepath': self.agency_certificate_filepath,
            'agency_registerdate': self.agency_registerdate,
            'agency_contact': self.agency_contact,
            'agency_state_id': self.agency_state_id,
            'agency_city_id': self.agency_city_id,
            'agency_login_id': self.agency_login_id
        }


db.create_all()
