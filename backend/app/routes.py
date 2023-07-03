from flask import jsonify, request
from app import app, db
from app.models import Task

@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        task = Task(description=data['description'])
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Task created!'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500
