"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from app import models
from flask import render_template, request, redirect, url_for,redirect,flash,send_from_directory
from .forms import PropertyForm
from werkzeug.utils import secure_filename
from app.models import PropertyInfo
from app import db
from sqlalchemy import exc

import os
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="real estate")

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/property/', methods = ['GET','POST'])
def property():
    """Render the website's form to add a new property. """
    form = PropertyForm()

    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        numberOfRooms = form.numberOfRooms.data
        numberOfBathrooms = form.numberOfBathrooms.data
        price = form.price.data
        propertyType = form.propertyType.data
        location = form.location.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        prop = PropertyInfo (title, description,numberOfRooms,numberOfBathrooms,price,location,propertyType,filename)

        db.session.add(prop)
        db.session.commit()
        
        

        flash("Property Successfully Added", "success")
        return redirect(url_for('properties'))

    return render_template('propertyform.html', form=form)

@app.route('/properties', methods= ['GET'])
def properties():
    """Renders a list of all properties in the database"""
    allProps = PropertyInfo.query.all()
    if request.method == 'GET':
    #propsAll = []

    #for i in propsAll:
        #propsAll.append({"id":i.id, "title":i.title, "price":i.price, "location":i.location, "photo":i.photo}) 
        
        return render_template('properties.html', properties=allProps)

@app.route('/property/<propertyid>', methods = ['GET'])
def pid(propertyid):
    """Renders the template for viewing an individual property by a specific  property id"""
    prec = PropertyInfo.query.filter_by(id = propertyid).first()
    if request.method == 'GET':
        return render_template('propertyid.html', properties = prec)


@app.route('/upload/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']),filename)


# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
