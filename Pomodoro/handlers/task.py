from fastapi import FastAPI, APIRouter, status, Depends
from pydantic import BaseModel
from typing import Annotated
from dependency import get_tasks_repository, get_cache_tasks_repository
from fixtures import tasks as fixtures_tasks
from schema  import TaskSchema
from database.database import get_db_session
from Repository import TaskRepository, TaskCache

router = APIRouter(prefix="/task", tags=["task"])
    
@router.get("/all", response_model = list[TaskSchema])
async def get_tasks(
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)],
    task_cache: Annotated[TaskCache, Depends(get_cache_tasks_repository)]
):
    tasks = task_repository.get_tasks()
    tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
    task_cache.set_tasks(tasks_schema)
    return tasks



@router.post("/create_task", response_model=TaskSchema)
async def create_task(task: TaskSchema, 
                      task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task




@router.patch("/{task_id}", response_model=TaskSchema)
async def patch_task(task_id: int, 
                     name: str,
                     task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_task_name(task_id, name)
  
        
        
            
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int,
                      task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.delete_task(task_id)
    return {"message": "task has been deleted"}
    