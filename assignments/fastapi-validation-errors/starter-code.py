from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API: Validation and Errors")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    completed: bool = False


tasks = [
    {"id": 1, "title": "Write API docs", "completed": False},
    {"id": 2, "title": "Test input validation", "completed": False},
]


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    normalized = task.title.strip().lower()
    for existing in tasks:
        if existing["title"].strip().lower() == normalized:
            raise HTTPException(status_code=400, detail="Task title already exists")

    next_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {"id": next_id, "title": task.title.strip(), "completed": task.completed}
    tasks.append(new_task)
    return new_task
