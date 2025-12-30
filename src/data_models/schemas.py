from datetime import date, datetime

from pydantic import BaseModel
from sqlmodel import SQLModel, Field, create_engine

engine = create_engine("sqlite:///habit.db")

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class Habit(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    metric_type: str
    target_minutes: int
    target_focus_score: int
    frequency: str
    is_frozen: bool = True

class HabitLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    habit_id: int = Field(foreign_key="habit.id")
    value_minutes: int
    value_focus_score: int
    log_date: date
    create_at: datetime = Field(default_factory=datetime.now)

class HabitLogCreate(BaseModel):
    value_minutes: int
    value_focus_score: int
    log_date: date | None = None

class HabitSummary(BaseModel):
    total_days: int
    logged_days: int
    missed_days: int
    consistency_percentage: float
    avg_minutes_value: float
    avg_focus_score_value: float