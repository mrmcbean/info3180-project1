from . import db

class PropertyInfo(db.Model):

    __tablename__ = "property"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(800))
    numberOfRooms = db.Column(db.String(20))
    numberOfBathrooms = db.Column(db.String(20))
    price = db.Column(db.String(80))
    location = db.Column(db.String(200))
    propertyType = db.Column(db.String(80))
    photo = db. Column(db.String(80))

    def __init__(self, title, description, numberOfRooms,numberOfBathrooms,price, location, propertyType, photo):
        self.title = title
        self.description = description
        self.numberOfRooms = numberOfRooms
        self.numberOfBathrooms = numberOfBathrooms
        self.price = price
        self.location = location
        self.propertyType = propertyType
        self.photo = photo


   
    def get_id(self):
        try:
            return unicode(self.id) #python 2 support
        except NameError:
            return str(self.id) #python 3 support


