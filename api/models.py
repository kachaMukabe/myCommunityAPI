from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


class CommunityEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(256))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    organizer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class AssistanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    assistance_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship(User, backref="requests")

    def __init__(self, description, assistance_type, user_id):
        self.description = description
        self.assistance_type = assistance_type
        self.user_id = user_id
