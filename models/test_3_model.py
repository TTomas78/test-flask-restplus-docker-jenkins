from app import db

class test432Model(db.Model):

    __tablename__ = 'conditio23ns'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_counter = db.Column(db.SmallInteger()