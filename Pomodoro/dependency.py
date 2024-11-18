from fastapi import Depends
from database import get_db_session
from Repository import TaskRepository, TaskCache
from service.task_service import TaskService
from cache import get_redis_connection

def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)

def get_cache_tasks_repository() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(redis_connection)


def get_tasks_service(
        tas_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: TaskCache = Depends(get_cache_tasks_repository)
    ) -> TaskService:
    
    return TaskService(
        task_repository=get_tasks_repository(),
        task_cache=get_cache_tasks_repository()
    )
    