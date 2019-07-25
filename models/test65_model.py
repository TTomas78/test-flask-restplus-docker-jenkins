from app import db

class Client43Model(db.Model):
    __tablename__ = 'accounts'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address1 = db.Column(db.String(100))
    address3 = db.Column(db.String(100))
    zip_code = db.Column(db.String(50))
    city = db.Column(db.String(100))
    # state = db.Column(db.String(100))