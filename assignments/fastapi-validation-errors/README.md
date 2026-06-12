# 📘 Assignment: FastAPI Validation and Error Handling

## 🎯 Objective

Improve a FastAPI project by adding strong input validation and clear error responses. You will learn how to use Pydantic models, HTTP exceptions, and status codes to build reliable APIs.

## 📝 Tasks

### 🛠️	Validate Request Data

#### Description
Create and apply request models so the API only accepts valid task data. Invalid requests should return helpful validation messages automatically.

#### Requirements
Completed program should:

- Define a Pydantic model for creating tasks with required fields and sensible defaults.
- Reject invalid input such as empty titles or invalid data types.
- Keep the project Python-only and use in-memory storage (no database setup).


### 🛠️	Return Clear API Errors

#### Description
Add endpoint logic that returns consistent responses for common error cases, including missing resources and duplicate task titles.

#### Requirements
Completed program should:

- Return HTTP 404 when a task id does not exist.
- Return HTTP 400 when a duplicate task title is submitted.
- Return clear JSON error messages and appropriate status codes for success and failure cases.
