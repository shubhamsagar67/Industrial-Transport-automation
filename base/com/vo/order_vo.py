from base import db
from base.com.vo.agency_vo import AgencyVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.quotation_vo import QuotationVO


class OrderVO(db.Model):
    __tablename__ = 'order_table'
    order_id = db.Column('order_id', db.Integer, primary_key=True,
                         autoincrement=True)
    order_quotation_id = db.Column('order_quotation_id', db.Integer,
                                   db.ForeignKey(QuotationVO.quotation_id,
                                                 ondelete='CASCADE',
                                                 onupdate='CASCADE'))
    order_datetime = db.Column('order_datetime', db.DateTime, nullable=False)
    order_login_id = db.Column('order_login_id', db.Integer,
                               db.ForeignKey(LoginVO.login_id,
                                             ondelete='CASCADE',
                                             onupdate='CASCADE'))
    order_agency_id = db.Column('order_agency_id', db.Integer,
                                db.ForeignKey(AgencyVO.agency_id,
                                              ondelete='CASCADE',
                                              onupdate='CASCADE'))

    def as_dict(self):
        return {
            'order_id': self.order_id,
            'order_quotation_id': self.order_quotation_id,
            'order_datetime': self.order_datetime,
            'order_login_id': self.order_login_id,
            'order_agency_id': self.order_agency_id
        }


db.create_all()
