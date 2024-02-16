from base import db


class TransporttypeVO(db.Model):
    __tablename__ = 'transporttype_table'
    transporttype_id = db.Column('transporttype_id', db.Integer,
                                 primary_key=True, autoincrement=True)
    transporttype_name = db.Column('transporttype_name', db.String(100),
                                   nullable=False)
    transporttype_description = db.Column('transporttype_description',
                                          db.String(100), nullable=False)

    def as_dict(self):
        return {
            'transporttype_id': self.transporttype_id,
            'transporttype_name': self.transporttype_name,
            'transporttype_description': self.transporttype_description
        }


db.create_all()
