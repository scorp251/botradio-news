from .database import db

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    body = db.Column(db.String(255))
    url = db.Column(db.String(255))
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    tags = db.relationship('Tag', secondary='article_tags')

    def __init__(self, title, body, url, image, published_at):
        self.title = title
        self.body = body
        self.url = url
        self.image = image
        self.created_at = created_at

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'url': self.url,
            'image': self.image,
            'created_at': self.created_at,
            'tags': [t.serialize() for t in self.tags]
        }

    def __repr__(self):
        return '<Article %r>' % self.title
