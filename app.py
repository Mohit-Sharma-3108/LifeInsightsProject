from datetime import date, datetime, timedelta
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select

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

engine = create_engine("sqlite:///habit.db")
app = FastAPI(title="Single Habit Tracker MVP")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

    # Bootstrap single user + habit if not exists
    with Session(engine) as session:
        user = session.exec(select(User)).first()
        if not user:
            user = User(name="Mohit")
            session.add(user)
            session.commit()
            session.refresh(user)

        habit = session.exec(select(Habit)).first()
        if not habit:
            habit = Habit(
                name="Focussed work on habit tracker project",
                metric_type="minutes and focus score",
                target_minutes=60,
                target_focus_score=6,
                frequency="daily"
            )
            session.add(habit)
            session.commit()


@app.post("/log")
def log_habit(payload: HabitLogCreate):
    log_date = payload.log_date or date.today()

    with Session(engine) as session:
        user = session.exec(select(User)).first()
        habit = session.exec(select(Habit)).first()

        existing = session.exec(
            select(HabitLog).where(HabitLog.log_date == log_date)
        ).first()

        if existing:
            raise HTTPException(status_code=400, detail="Log already exists for this date")
        
        log = HabitLog(
            user_id=user.id,
            habit_id=habit.id,
            value_minutes=payload.value_minutes,
            value_focus_score=payload.value_focus_score,
            log_date=log_date
        )
        session.add(log)
        session.commit()

    return {"status": "logged", "date": log_date}

@app.get("/summary", response_model=HabitSummary)
def get_summary(days: int=14):
    end_date = date.today()
    start_date = end_date - timedelta(days=days - 1)

    with Session(engine) as session:
        logs = session.exec(
            select(HabitLog).where(HabitLog.log_date >= start_date)
        ).all()

    logged_days = len({log.log_date for log in logs})
    total_days = days
    missed_days = total_days - logged_days

    avg_minutes_value = sum([log.value_minutes for log in logs]) / logged_days if logged_days else 0
    avg_focus_score = sum([log.value_focus_score for log in logs]) / logged_days if logged_days else 0

    consistency_percentage = (logged_days / total_days) * 100

    return HabitSummary(
        total_days=total_days,
        logged_days=logged_days,
        missed_days=missed_days,
        consistency_percentage=round(consistency_percentage, 2),
        avg_minutes_value=round(avg_minutes_value, 2),
        avg_focus_score_value=round(avg_focus_score, 2)
    )