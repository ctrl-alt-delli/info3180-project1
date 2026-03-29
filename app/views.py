from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
import os


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        property = Property(
            title=form.title.data,
            description=form.description.data,
            no_of_rooms=form.no_of_rooms.data,
            no_of_bathrooms=form.no_of_bathrooms.data,
            price=form.price.data,
            property_type=form.property_type.data,
            location=form.location.data,
            photo=filename
        )
        db.session.add(property)
        db.session.commit()

        flash('Property successfully added!', 'success')
        return redirect(url_for('properties'))

    return render_template('create_property.html', form=form)


@app.route('/properties')
def properties():
    all_properties = Property.query.all()
    return render_template('properties.html', properties=all_properties)


@app.route('/properties/<int:propertyid>')
def property_detail(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('property_detail.html', property=property)

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# Helper functions
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404