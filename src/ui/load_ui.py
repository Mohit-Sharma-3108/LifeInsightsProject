import streamlit as st

st.set_page_config(page_title="CRUD app UI", layout="wide")
st.header("CRUD app UI")
goal = st.text_input("What is the goal that you are working towards?", placeholder="E.g Build a muscular body")

st.divider()

num_habits = st.slider(
    "How many habits do you want to track for this goal?",
    min_value=1,
    max_value=5,
    value=1
)

habits = []

for i in range(num_habits):
    st.subheader(f"Habit {i+1}")
    habit_name = st.text_input(
        f"Habit {i+1}",
        placeholder="E.g Go to the gym for 6o mins",
        key=f"habit_name_{i}"
    )
    habits.append({
        "habit_name": habit_name,
        "metrics": []
    })

st.divider()

st.subheader("How do you want to measure each habit?")

for i, habit in enumerate(habits):
    st.markdown(f"Habbit: **{habit['habit_name'] or 'Unnamed habbit'}**")

    num_metrics = st.number_input(
        f"How many metrics for '{habit['habit_name'] or 'this habit'}'?",
        min_value=1,
        max_value=3,
        step=1,
        key=f"num_metrics_{i}"
    )

    metrics = []

    for j in range(num_metrics):
        col1, col2 = st.columns(2)

        with col1:
            metric_name = st.text_input(
                f"Metric {j+1} name",
                placeholder="e.g Duration",
                key=f"metric_name_{i}_{j}"
            )
        with col2:
            metric_type = st.text_input(
                f"Metric value",
                placeholder="e.g if duration can be number of minutes...",
                key=f"metric_type_{i}_{j}"
            )

        metrics.append({
            "metric_name": metric_name,
            "metric_type": metric_type
        })

    habits[i]["metrics"] = metrics

st.divider()

habit_definition = {
    "goal": goal,
    "habits": habits
}


st.subheader("Generated defintion (JSON)")
st.json(habit_definition)

if st.button("Save"):
    st.success("Definition ready to save to DB")
