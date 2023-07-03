from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Define the User model
class User(db.Model):
    # Define the columns for the User table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    email = db.Column(db.String(120), nullable=False)  # Email address for the user
    password_hash = db.Column(db.String(128))  # Hashed password for the user

    # Method to set the hashed password
    def set_password(self, password):
        # Generate a hashed version of the password and store it
        self.password_hash = generate_password_hash(password)

    # Method to check the hashed password
    def check_password(self, password):
        # Hash the input password and compare it to the stored hash
        return check_password_hash(self.password_hash, password)
    
    # Method to get user id
    def get_id(self):
        return self.id

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to link the task to a user
    description = db.Column(db.String(80), nullable=False)
