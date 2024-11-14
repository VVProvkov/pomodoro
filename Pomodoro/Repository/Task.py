from sqlalchemy import select
from sqlalchemy.orm import Session
from database import Tasks, Categories, get_db_session
from schema import TaskSchema
class TaskRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def get_tasks(self):
        with self.db_session() as session:
            task: list[Tasks] = session.execute(select(Tasks)).scalars().all()
        return task
        
    def get_task(self, task_id: int):
        with self.db_session() as session:
            task: list[Tasks] = session.execute(select(Tasks).where(Tasks.id == task_id)).scalars_one_or_none()
        return task
    
    def create_task(self, task:TaskSchema) -> None:
        task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
            
    def delete_task(self, task_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            session.execute(query)
            session.commit()
            
    def get_task_by_category_name(self, category_name: str) -> list[Tasks]:
        query = select(Tasks).join(Categories, Tasks.category_id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            task: list[Tasks] = session.execute(query).scalars().all()
            return task
    