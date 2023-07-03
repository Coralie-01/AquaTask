from flask import jsonify, request
from app import app, db
from app.models import Task

# Define a route for creating tasks, which accepts POST requests
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json() # Get data from POST request
        task = Task(description=data['description']) # Create task
        db.session.add(task) # Add task to database
        db.session.commit() # Commit changes
        return jsonify({'message': 'Task created!'}) # Return success message
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500
