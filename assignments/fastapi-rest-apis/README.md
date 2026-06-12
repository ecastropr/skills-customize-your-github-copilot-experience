# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and Python. You will learn how to define API routes, handle request and response data, and return clear HTTP status codes.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI application and implement the core endpoints for a small task manager API. Your API should let users test the server, list tasks, and add new tasks.

#### Requirements
Completed program should:

- Create a FastAPI app and run it with Uvicorn.
- Implement a GET endpoint at / that returns a welcome message.
- Implement GET /tasks to return a list of tasks.
- Implement POST /tasks to add a new task from JSON request data.


### 🛠️	Add Resource Lookup and Error Handling

#### Description
Extend the API so users can fetch a single task by id and receive helpful error responses when a task does not exist.

#### Requirements
Completed program should:

- Implement GET /tasks/{task_id} to return one task.
- Return HTTP 404 with a clear message if task_id is not found.
- Return appropriate status codes for successful and unsuccessful requests.
