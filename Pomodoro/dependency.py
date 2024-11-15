from database import get_db_session
from Repository import TaskRepository, TaskCache
from cache import get_redis_connection

def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)

def get_cache_tasks_repository() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(get_redis_connection)
