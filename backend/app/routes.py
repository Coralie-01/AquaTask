from flask import jsonify, request
from app import app, db
from app.models import Task, User
from werkzeug.security import generate_password_hash, check_password_hash

# Define a route for creating tasks, which accepts POST requests
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json() # Get data from POST request
        user_id = data['user_id']
        desc = data['description']
        task = Task(description=desc,user_id=user_id) # Create task
        db.session.add(task) # Add task to database
        db.session.commit() # Commit changes
        return jsonify({'message': 'Task created!'}) # Return success message
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500

# Define a route for register a user
@app.route('/register', methods=['POST'])
def register():
    print("Registering user...")
    try:
        data = request.get_json() # Get data from POST request
        email = data['email']
        password = data['password']
        print(f"Email: {email}")
        # Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'User already exists!'}), 400
    
        # Create user
        new_user = User(email=email)
        new_user.set_password(password)

        # Add user to database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created!'}), 201
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500

# Define a route for signing in a user
@app.route('/auth', methods=['POST'])
def auth():
    try:
        data = request.get_json() # Get data from POST request
        email = data['email']
        password = data['password']
        
        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'message': 'User does not exist!'}), 400
    
        # Check if password is correct
        if not user.check_password(password):
            return jsonify({'message': 'Incorrect password!'}), 400

        return jsonify({'message': 'User signed in!', 'user_id' : user.get_id()}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500


