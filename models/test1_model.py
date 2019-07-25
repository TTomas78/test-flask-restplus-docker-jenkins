from app import db

class ClientModel(db.Model):
    __tablename__ = 'client_accounts'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))
    zip_code = db.Column(db.String(50))
    city = db.Column(db.String(100))
    # state = db.Column(db.String(100))