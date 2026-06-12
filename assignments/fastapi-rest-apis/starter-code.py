from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


# Starter in-memory data. Students can add, edit, or replace this.
tasks = [
    {"id": 1, "title": "Read FastAPI docs", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    next_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {"id": next_id, "title": task.title, "completed": task.completed}
    tasks.append(new_task)
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")
