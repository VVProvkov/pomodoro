from pydantic import BaseModel, Field, model_validator, ValidationInfo

class Task(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(exclude=True)

   