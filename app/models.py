# Add any model classes for Flask-SQLAlchemy here
from . import db

class Movies(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.Text)
    posterName = db.Column(db.String(100))
    date_created = db.Column(db.DateTime,default=db.func.current_timestamp() )
    
    def __init__(self,title,desc,posterName):
        self.title= title
        self.desc = desc
        self.posterName = posterName
        
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<movie %r>' % (self.id)