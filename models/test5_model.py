from app import db

class TestModel(db.Model):

    __tablename__ = 'test_table'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))