# routes.py

from flask import render_template, url_for, flash, redirect
from werkzeug.utils import secure_filename
from PIL import Image
import os

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_image():
    form = ImageUploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image = Image.open(image_file)
        image.thumbnail((300, 300))
        image.save(filepath)

        new_image = Image(filename=filename, owner=current_user)
        db.session.add(new_image)
        db.session.commit()

        flash('Image uploaded successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('upload.html', form=form)
