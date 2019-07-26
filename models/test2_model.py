from app import db

class ConditionModel(db.Model):

    __tablename__ = 'conditions'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cutoff = db.Column(db.SmallInteger())
#    max_lead_time = db.Column(db.SmallInteger())
 #   length_of_stay = db.Column(db.SmallInteger())
    min_room_allotment = db.Column(db.SmallInteger())
    max_room_allotment = db.Column(db.SmallInteger())
    min_occupancy = db.Column(db.SmallInteger())
    #max_occupancy = db.Column(db.SmallInteger())
    booking_counter = db.Column(db.SmallInteger())
    custom = db.Column(db.String(100))
