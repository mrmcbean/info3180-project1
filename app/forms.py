from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields import TextAreaField,SelectField
from flask_wtf.file import FileField, FileRequired,FileAllowed

class PropertyForm(FlaskForm):

    title = StringField('Property Title', validators = [DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    numberOfRooms = StringField('No. of Rooms',validators=[DataRequired()])
    numberOfBathrooms = StringField('No. of Bathrooms',validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    propertyType = SelectField('Property Type', choices =[("None", "Select Type"),("House","House"), ("Apartment", "Apartment")], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators = [FileRequired(),
                                            FileAllowed(["jpg","png","jpeg"], "Images only")])
