from interaction import db

class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.Text, nullable=False)
    response_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Interaction('{self.input_text}', '{self.response_text}')"

    def save(self):
        db.session.add(self)
        db.session.commit()
