import streamlit as st
from datetime import datetime, date

GOALS = [
    {
        "goal_name": "Build habit logging app",
        "phases": [
            {
                "phase_name": "MVP skeleton",
                "habits": [
                    {
                        "habit_name": "Write core streamlit pages",
                        "measures": [
                            {
                                "metric_name": "Duration",
                                "unit": "minutes",
                                "daily_target": 60,
                            },
                            {
                                "metric_name": "Focus_score",
                                "unit": "score out of 10",
                                "daily_target": 7
                            }
                        ]
                    },
                    {
                        "habit_name": "Add agent on page 1 to help form SMART goal",
                        "measures": [
                            {
                                "metric_name": "Duration",
                                "unit": "minutes",
                                "daily_target": 90
                            },
                            {
                                "metric_name": "Number of commits",
                                "unit": "commits",
                                "daily_target": 2
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

REASON_CATEGORIES = [
    "Time constraints",
    "Low energy / health",
    "Distraction",
    "Poor planning",
    "External obligation",
    "Other"
]

st.set_page_config(page_title="Daily logging", layout="centered")

today = date.today()
st.caption(f"Logging for: {today}")

# Goal selection
goal_names = [goal["goal_name"] for goal in GOALS]  # This will return ["Build habit logging app"]

selected_goal_name = st.selectbox("Select goal", goal_names)

selected_goal = next(
    goal for goal in GOALS if goal["goal_name"] == selected_goal_name
)   # This will return dictionary with goal_name as "Build habit logging app"

# Phase selection
phase_name = [phase["phase_name"] for phase in selected_goal["phases"]]  # This will return ["MVP skeleton"]

selected_phase_name = st.selectbox("Select phase", phase_name)

selected_phase = next(
    phase for phase in selected_goal["phases"] if phase["phase_name"] == selected_phase_name
)  # This will return a dictionary with phase_name as "MVP skeleton"

""" selected_goal is a dictionary with relevant goal
    phase_name is a list with all the phase_names in the form of a list
    selected_phase_name is a string with the relevant phase_name
    selected_goal[selected_phase_name]
"""

# Habit selection
habit_names = [h["habit_name"] for h in selected_phase["habits"]]  # This will return ["Write core streamlit pages", "Add agent on page 1 to help form SMART goal"]

selected_habit_name = st.selectbox("Select Habit", habit_names)

selected_habit = next(
    h for h in selected_phase["habits"] if h["habit_name"] == selected_habit_name
)  # This will return a dictionary with habit_name as "Write core streamlit pages"

st.divider()

# Measure logging
st.subheader("Log today's work...")

measure_inputs = {}
met_all_measures = True

for measure in selected_habit["measures"]:
    value = st.number_input(
        f"{measure['metric_name']} ({measure['unit']})",
        min_value=0,
        step=5
    )

    measure_inputs[measure["metric_name"]] = value

    if value < measure["daily_target"]:
        met_all_measures = False

# If not met -> ask constraints
reason_category = None
reason_text = None

if not met_all_measures:
    st.warning("Daily target not met")

    reason_category = st.selectbox(
        "What limited you today",
        REASON_CATEGORIES
    )

    if reason_category == "Other":
        reason_text = st.text_input(
            "Please provide more details",
            placeholder="Briefly describe what happened"
        )

    else:
        reason_text = st.text_input(
            "Anything else you want to add? (Optional)",
        )
    

if st.button("Save log"):
    log_entry = {
        "date": today,
        "timestamp": datetime.now(),
        "goal": selected_goal_name,
        "phase": selected_phase_name,
        "habit": selected_habit_name,
        "measures": measure_inputs,
        "success": met_all_measures,
        "reason_category": reason_category,
        "reason_text": reason_text
    }

    st.success("Log saved")
    st.json(log_entry)


