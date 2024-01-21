from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
admin = Admin(app)

# Define your models here (e.g., User, Image)

class User(db.Model):
    # ...

class Image(db.Model):
    # ...

# Add your models to the admin panel
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Image, db.session))

if __name__ == '__main__':
    app.run(debug=True)
