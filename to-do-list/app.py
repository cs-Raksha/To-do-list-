from flask import Flask, render_template, request, redirect#redirect for redirecting to different routes.

app = Flask(__name__)  # Create a Flask application instance

tasks = []  # Initialize an empty list to store tasks

@app.route('/')  # Define the root URL route
def index():  # Function to render index page
    return render_template('index.html', tasks=tasks)  # Render index.html template with tasks

@app.route('/add', methods=['POST'])  # Define route to add a new task
def add_task():  # Function to add a new task  
    task = request.form['task']  # Get task data from form
    tasks.append(task)  # Add task to the list
    return redirect('/')  # Redirect back to the root URL

@app.route('/edit/<int:index>', methods=['GET', 'POST'])  # Define route to edit a task
def edit(index):  # Function to edit a task
    if request.method == 'POST':  # Check if form submitted
        tasks[index] = request.form['task']  # Update task with new data
        return redirect('/')  # Redirect back to the root URL
    return render_template('edit.html', index=index, task=tasks[index])  # Render edit.html template

@app.route('/update/<int:index>', methods=['POST'])  # Define route to update a task
def update(index):  # Function to update a task
    tasks[index] = request.form['task']  # Update task with new data
    return redirect('/')  # Redirect back to the root URL

@app.route('/delete/<int:index>')  # Define route to delete a task
def delete(index):  # Function to delete a task
    tasks.pop(index)  # Remove task from the list
    return redirect('/')  # Redirect back to the root URL

@app.route('/complete/<int:index>')  # Define route to mark a task as complete
def complete(index):  # Function to mark a task as complete
    tasks[index] = '✓ ' + tasks[index]  # Add checkmark to task
    return redirect('/')  # Redirect back to the root URL

if __name__ == '__main__':  # Check if script is executed directly
    app.run(debug=True)  # Start the Flask application in debug mode