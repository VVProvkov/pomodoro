from fastapi import FastAPI, APIRouter, status
from pydantic import BaseModel
from fixtures import tasks as fixtures_tasks
from schema.task import Task
from database import get_db_connection

router = APIRouter(prefix="/task", tags=["task"])
    
@router.get("/all", response_model = list[Task])
async def get_tasks():
    result: list[Task] = []
    cursor = get_db_connection().cursor()
    tasks = cursor.execute("SELECT * FROM tasks;").fetchall()
    for task in tasks:
        result.append(Task(
            id=task[0],
            name=task[1],
            pomodoro_count=task[2],
            category_id=task[3]         
        ))
    return result

@router.post("/create_task", response_model=Task)
async def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (name, pomodoro_count, category_id) VALUES (?,?,?)",
                   (task.name, task.pomodoro_count, task.category_id))
    connection.commit()
    connection.close()
    fixtures_tasks.append(task)
    return task

@router.patch("/{task_id}", response_model=Task)
async def patch_task(task_id: int, name: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks set name =? WHERE id =?", (name, task_id))
    connection.commit()
    task = cursor.execute("SELECT * FROM tasks WHERE id =?", f"{task_id}").fetchall()[0] 
    connection.close()   
    return Task(
        id=task[0],
        name=task[1],
        pomodoro_count=task[2],
        category_id=task[3]     
    )
            
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id =?", (task_id,))
    connection.commit()
    connection.close()   
    return {"message": "task has been deleted"}
    
    
    
    
    for index, task in enumerate(fixtures_tasks):
        if task["id"] == task_id:
           del fixtures_tasks[index]
           return {"message": "task is deleted"}
    return {"message": "task is not found"}