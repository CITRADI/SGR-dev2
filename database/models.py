from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    contact_info = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class InteractionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_input = db.Column(db.String(200))
    ai_feedback = db.Column(db.String(200))

class WritingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100))
    topic = db.Column(db.String(200))
    communicative_intent = db.Column(db.String(200))
    goal = db.Column(db.String(200))
    central_idea = db.Column(db.String(200))
    audience = db.Column(db.String(200))
    status = db.Column(db.String(50))

class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    contact_info = db.Column(db.String(200))
