from app import db

class testingmd(db.Model):
    __tablename__ = 'modelss'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address3 = db.Column(db.String(100))
    city = db.Column(db.String(100))
    # state = db.Column(db.String(100))