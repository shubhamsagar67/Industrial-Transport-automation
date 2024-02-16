from base import db
from base.com.vo.request_vo import RequestVO


class QuotationVO(db.Model):
    __tablename__ = 'quotation_table'
    quotation_id = db.Column('quotation_id', db.Integer, primary_key=True,
                             autoincrement=True)
    quotation_price = db.Column('quotation_price', db.Integer, nullable=False)
    quotation_delivery_duration = db.Column('quotation_delivery_duration',
                                            db.Integer, nullable=False)
    quotation_comment = db.Column('quotation_comment', db.String(255),
                                  nullable=False)
    quotation_status = db.Column('quotation_status', db.String(25),
                                 nullable=False)
    quotation_datetime = db.Column('quotation_datetime', db.DateTime,
                                   nullable=False)
    quotation_request_id = db.Column('quotation_request_id', db.Integer,
                                     db.ForeignKey(RequestVO.request_id,
                                                   ondelete='CASCADE',
                                                   onupdate='CASCADE'))

    def as_dict(self):
        return {
            'quotation_id': self.quotation_id,
            'quotation_price': self.quotation_price,
            'quotation_comment': self.quotation_comment,
            'quotation_delivery_duration': self.quotation_delivery_duration,
            'quotation_status': self.quotation_status,
            'quotation_datetime': self.quotation_datetime,
            'quotation_request_id': self.quotation_request_id
        }


db.create_all()
