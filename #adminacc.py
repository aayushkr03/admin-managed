from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from your_app.models import User  # Import your User model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

def initialize_admin_account():
    # Check if the admin account already exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        # If not, create the admin account
        hashed_password = generate_password_hash('admin_password', method='sha256')
        admin = User(username='admin', password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        print('Admin account created successfully!')
    else:
        print('Admin account already exists.')

if __name__ == '__main__':
    with app.app_context():
        initialize_admin_account()
