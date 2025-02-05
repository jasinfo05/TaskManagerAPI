# Task_Manager_API

The Task Manager API is a Django-based web application that allows users to manage their tasks efficiently. The API provides features such as task creation, updating, deletion (soft delete), pagination, filtering, and searching. It is built using Django Rest Framework and includes the feature task status management.

## Features
- **CRUD Operations**: Create, Retrieve, Update, Delete tasks.
- **Soft Deletion**: Tasks can be soft deleted (marking them as deleted without actually removing them from the database).
- **Pagination**: Supports pagination for task listings.
- **Filtering & Sorting**: Filter tasks by status, created date, and sort tasks in ascending and descending order with created date.
- **Search**: Search tasks by title and description.

## Tech Stack
- **Backend**: Django 5.1.5, Django Rest Framework (DRF)
- **Database**: SQLite (for development)
- **Pagination**: Django Rest Framework pagination
- **API Documentation**: DRF browsable API interface

## Installation
1. Install Python
Windows:

Download the latest version of Python from the official website: https://www.python.org/downloads/.

2. Install Virtual Environment 
Create a virtual environment to keep your dependencies isolated from other projects:

python -m venv myenv

Activate the virtual environment:

Windows: myenv\Scripts\activate

Mac/Linux: source myenv/bin/activate

3. Install Django
Once the virtual environment is activated, install Django using pip:

pip install django

4. Install Django Rest Framework (DRF)
Install Django Rest Framework to build your API:

pip install djangorestframework

### Prerequisites
Make sure you have Python installed on your machine. The following versions of Python and Django are supported:
- Python 3.x
- Django 5.1.5
- Django Rest Framework

### Clone the Repository
1. clone the repository from GitHub:

git clone https://github.com/jasinfo05/TaskManagerAPI.git

2. Navigate to the Project Directory

cd Task_Manager_API

3. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

python -m venv testenv

4. Activate the Virtual Environment

Windows:  testenv\Scripts\activate
Mac/Linux:  source testenv/bin/activate

5. Apply Database Migrations

Run the migrations to set up the database:

python manage.py makemigrations
python manage.py migrate

6. Run the Development Server
Run the server to start the application:

python manage.py runserver

The API should now be accessible at http://127.0.0.1:8000/taskapi/

Available Endpoints
GET /taskapi/: List all tasks with pagination.
POST /taskapi/: Create a new task.
GET /taskapi/{id}/: Retrieve a specific task by ID.
PUT /taskapi/{id}/: Update an existing task by ID.
DELETE /taskapi/{id}/: Soft delete a task by ID (mark as deleted).

Example API Request
Create a Task
POST /  http://127.0.0.1:8000/taskapi/

Request Body:

{
  "title": "Review PR #42",
  "description": "Implement the fix for restoring the deleted data.",
  "status": "Pending"
}

Get All Tasks
GET /  http://127.0.0.1:8000/taskapi/

Response:

example:
[
    {
        "id": 1,
        "title": "Review PR #42",
        "description": ""Implement the fix for restoring the deleted data.",
        "status": "Pending",
        "created_at": "2025-02-05T10:00:00Z",
        "updated_at": "2025-02-05T10:00:00Z"
    }
]

Update a Task
PUT /  http://127.0.0.1:8000/taskapi/1/


Request Body:

{
  "title": "Review PR #42",
  "description": "Implement the fix for restoring the deleted data.",
  "status": "Complete"
}

Soft Delete a Task
DELETE / http://127.0.0.1:8000/taskapi/1/



