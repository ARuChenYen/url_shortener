from .extensions import db
import random

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(256))
    short_url = db.Column(db.String(7), unique=True)
    count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base62 = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.short_url = self.create_short()
        
    def create_short(self):
        short_url = []
        for _ in range(7):
            short_url.append(self.base62[random.randint(0,61)])
        short_url = ''.join(short_url)

        short_exist = self.query.filter_by(short_url=short_url).first()
        
        if short_exist:
            return self.create_short()
        
        return short_url

