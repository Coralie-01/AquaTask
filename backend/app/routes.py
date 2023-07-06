from datetime import datetime, timedelta
from flask import jsonify, request
from app import app, db
from app.models import Task, User
from werkzeug.security import generate_password_hash, check_password_hash

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




# Define a route for creating tasks, which accepts POST requests
@app.route('/tasks', methods=['GET', 'POST','PUT'])
def create_task():
    try:
        data = request.get_json() # Get data from POST request
        print("Creating task...")
        user_id = data['user_id']
        desc = data['description']
        cat = data['category']
        duedate = data['due_date']
        now = datetime.now()
        if (duedate == 'Today'):
            duedate = now
        elif (duedate == 'Tomorrow'):
            duedate = now + timedelta(days=1)
        elif (duedate == 'Next week'):
            duedate = now + timedelta(days=7)
        else:
            duedate = None
        task = Task(description=desc,user_id=user_id,category=cat,due_date=duedate, done=False) # Create task
        db.session.add(task) # Add task to database
        db.session.commit() # Commit changes
        return jsonify(task.as_dict()) # Return the description of the task and its ID
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500


 # Define a route for getting tasks
@app.route('/get/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    try:
        tasks = Task.query.filter_by(user_id=user_id,done=False).all() # Get all tasks for the user
        donetasks = Task.query.filter_by(user_id=user_id,done=True).all()
        task_list = [] # Create an empty list to store the tasks
        donetasks_list = []
        for task in tasks:
            task_list.append(task.as_dict()) # Add each task to the list
        for task in donetasks:
            donetasks_list.append(task.as_dict())
        return jsonify({'tasks': task_list, 'donetasks':donetasks_list}) # Return the list of tasks
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500 
  
# Define a route for updating tasks as done, which accepts PUT requests
@app.route('/updatetask', methods=['PUT'])
def update_task():
    try:
        data = request.get_json() # Get data from PUT request
        task_id = data['id']
        done_bool = data['done']
        task = Task.query.filter_by(id=task_id).first() # Get the task from the database
        task.done = done_bool # Update the task as done or unddone
        db.session.commit() # Commit changes
        return jsonify(task.as_dict()), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred'}), 500
    

# Route for adding/editing category of task.
@app.route('/taskcategory',methods=['PUT'])
def category_task():
    try:
        data = request.get_json()
        task_id, category = data['id'],data['category']
        task = Task.query.filter_by(id=task_id).first()
        task.category = category
        db.session.commit()
        return jsonify(task.as_dict()),200
    except Exception as e:
        return jsonify({'message': 'An error occurred'}), 500

# Route for adding/editing due date of a task.
@app.route('/taskduedate', methods=['PUT'])
def due_date_task():
    try:
        data = request.get_json()
        task_id, due_date = data['id'], data['due_date']
        task = Task.query.filter_by(id=task_id).first()
        task.due_date = due_date
        db.session.commit()
        return jsonify(task.as_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred'}), 500
