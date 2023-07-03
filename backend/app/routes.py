from flask import jsonify, request
from app import app, db
from app.models import Task

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(description=data['task'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201
