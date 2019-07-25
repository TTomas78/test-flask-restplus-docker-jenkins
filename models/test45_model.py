from app import db

class TomasModel(db.Model):

    __tablename__ = 'bitcoins'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500))