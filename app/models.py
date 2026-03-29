from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    no_of_rooms = db.Column(db.Integer, nullable=False)
    no_of_bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)  # 'House' or 'Apartment'
    location = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, no_of_rooms, no_of_bathrooms, price, property_type, location, photo):
        self.title = title
        self.description = description
        self.no_of_rooms = no_of_rooms
        self.no_of_bathrooms = no_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo