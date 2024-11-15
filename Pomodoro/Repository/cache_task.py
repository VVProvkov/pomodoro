from redis import Redis
from schema import TaskSchema

class TaskCache: 
    def __init__(self, redis: Redis) -> None:
        self.redis = redis
        
        
    def get_tasks(self):
        pass

    def set_tasks(self, tasks: list[TaskSchema]): 
        tasks_json = [task.model_dump_json() for task in tasks]
        self.redis.set(name="tasks", value=tasks_json)