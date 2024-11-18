from redis import Redis
from schema import TaskSchema
import json

class TaskCache: 
    def __init__(self, redis: Redis) -> None:
        self.redis = redis
        
        
    def get_tasks(self) -> list[TaskSchema]:
        with self.redis as redis: 
            tasks_json =  redis.lrange("tasks", 0, -1)
            return [TaskSchema.model_validate(json.loads(task)) for task in tasks_json]

    def set_tasks(self, tasks: list[TaskSchema]): 
        tasks_json = [task.model_dump_json() for task in tasks]
        with self.redis as redis: 
            self.redis.lpush("tasks",*tasks_json)