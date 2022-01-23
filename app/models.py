from app import db
import datetime


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    net_id = db.Column(db.String(20), index=True)
    post_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    start_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    end_time = db.Column(db.DateTime, index=True, default=(datetime.datetime.utcnow() + datetime.timedelta(minutes=60)))
    duration = db.Column(db.Integer, index=True, default=60)
    title = db.Column(db.String(100))
    building = db.Column(db.String(50))
    room = db.Column(db.String(50))
    latitude = db.Column(db.Float(5))
    longitude = db.Column(db.Float(5))
    description = db.Column(db.String(500))

    def __repr__(self):
        return '<Event ID: {}>'.format(self.id)


class Picture(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    name = db.Column(db.String(1000))
    event_picture = db.Column(db.String(1000))
    public_id = db.Column(db.String(1000), primary_key=True)
    event = db.relationship('Event', backref=db.backref('pictures', cascade="all,delete", lazy='dynamic'))

    def __repr__(self):
        return '<Event ID: {}; Picture URL: {}>'.format(self.event_id, self.event_picture)

    __mapper_args__ = {
        'confirm_deleted_rows': False
    }


class FirstTime(db.Model):
    net_id = db.Column(db.String(20), primary_key=True)

    def __repr__(self):
        return '<User: {}>'.format(self.net_id)


class NotificationSubscribers(db.Model):
    net_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30))
    email_address = db.Column(db.String(30), default="")
    phone_number = db.Column(db.String(20), default="")
    wants_email = db.Column(db.Boolean, default=False)
    wants_text = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User: {}>'.format(self.net_id)
