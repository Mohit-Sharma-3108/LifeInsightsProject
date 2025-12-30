from src.data_models.schemas import HabitLog, engine
from sqlmodel import Session, select
from datetime import date, timedelta


def view_last_n_days_summary(days: int=14):        
        end_date = date.today()
        start_date = end_date - timedelta(days=days - 1)

        with Session(engine) as session:
            logs = session.exec(
                    select(HabitLog)
                    .where(HabitLog.log_date >= start_date)
                    .where(HabitLog.log_date <= end_date)
            ).all()
            if not logs:
                print("No records found...")
            
            log_map = {
                 log.log_date: (log.value_minutes, log.value_focus_score)
                 for log in logs
            }

            print("\nLast 14 Days Habit Summary\n")
            print(f"{'Date':<12} {'Minutes':<10} {'Focus':<8} Status")
            print("-" * 42)

            current = start_date
            while current <= end_date:
                data = log_map.get(current)

                if data is not None:
                    minutes, focus_score = data
                    print(
                        f"{current} "
                        f"{str(minutes):<10} "
                        f"{str(focus_score):<8} ✔"
                    )
                else:
                    print(
                        f"{current} "
                        f"{'—':<10} "
                        f"{'—':<8} ✖"
                    )

                current += timedelta(days=1)


if __name__ == "__main__":
    view_last_n_days_summary()