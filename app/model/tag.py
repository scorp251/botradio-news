from .database import db

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # article = db.relationship('Article', secondaly='article_tags')

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return "<Tag {self.name}>"
