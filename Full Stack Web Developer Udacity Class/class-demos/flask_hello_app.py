# Import Dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Not used currently

# Initiate Flask App
app = Flask(__name__)

# Configure the database URI with the local database called "example"
# The format is:  dialect://username:password@host:portNumber/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://THEJAGSTER@localhost:5432/example'

# Stop SQLAlchemy Track Modifications since it will be depreciated soon
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a class and name the table while adding two columns
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # Add a Dunder Method __repr__ to allow for printing Table info
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

# Detects models and creates tables for them
db.create_all()

# Add Python decorator for Flask to assign URLs
# The decorator tells @app that whenever a user visits the app domain
# at the given .route(), execute the home() function
@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

