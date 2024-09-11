
from flask_sqlalchemy import  SQLAlchemy
from flask import  url_for

db = SQLAlchemy()



class book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(80))
    pages = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return url_for('static', filename=f"book/images/{self.image}")

    @property
    def show_url(self):
        return url_for('book.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('book.delete', id=self.id)
