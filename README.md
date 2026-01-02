# Goal Achievement & Habit Tracking Platform

A structured goal-setting and habit-tracking application that transforms vague ambitions into measurable, trackable outcomes using AI-assisted planning and data-driven progress insights.

---

## Overview

Many people fail to achieve their goals not because of a lack of motivation, but due to poor goal definition, unclear tracking, and lack of structured reflection.

This project aims to solve that by:
- Converting vague goals into SMART goals
- Breaking goals into phases, habits, and measurable metrics
- Logging daily execution and failures with context
- Providing weekly and monthly progress insights

The product is designed to be minimal, intentional, and focused on behavioral consistency over motivation.

---

## Core Concept

The application follows a three-page architecture, where each page represents a critical stage of goal achievement:

1. Goal Definition & Planning  
2. Daily Execution & Logging  
3. Progress Analysis & Reflection  

---

## Application Pages

### Page 1: Goal Definition & Structuring

This page helps users convert a vague intention into a clear, executable plan.

**Features:**
- User enters a high-level, vague goal (e.g., "get fit", "learn ML")
- An LLM/agent converts the vague goal into a SMART goal
- The SMART goal is automatically broken down into:
  - Phases (major milestones)
  - Habits (repeatable actions)
  - Measures (quantifiable metrics such as duration, count, or completion)

**Outcome:**
A structured, trackable goal hierarchy that removes ambiguity from execution.

---

### Page 2: Daily Logging & Core Logic

This page acts as the operational core of the product.

**Features:**
- Users log daily activity for each habit and measure
- Logged data is validated and persisted in a database
- If a daily target is not met, the user can:
  - Record the reason for failure
  - Store contextual information such as lack of time, fatigue, or motivation

**Outcome:**
A comprehensive dataset capturing both performance and behavioral friction.

---

### Page 3: Progress Dashboard & Insights

This page focuses on reflection, accountability, and progress analysis.

**Features:**
- Weekly and monthly progress summaries
- Habit adherence trends over time
- Phase-wise and goal-level completion tracking
- Insights into:
  - Consistency patterns
  - Missed targets
  - Common failure reasons

**Outcome:**
Users gain clarity on how they are progressing, not just whether they are progressing.

---

## High-Level Data Model

- Goal  
  - SMART goal definition
- Phases  
  - Milestones linked to a goal
- Habits  
  - Actions linked to phases
- Measures  
  - Quantifiable targets for each habit
- Daily Logs  
  - Actual performance data
  - Optional failure reasons
- Aggregations  
  - Weekly and monthly summaries

---

## Planned Tech Stack

- Frontend: Streamlit
- Backend Logic: Python
- Database: SQLite / PostgreSQL
- AI Layer: LLM-based agent for SMART goal generation
- Visualization: Streamlit charts and tables

---

## Future Enhancements

- Pattern detection in failure reasons
- AI-generated weekly and monthly reviews
- Goal adjustment suggestions based on historical progress
- Streak tracking and behavioral nudges
- Exportable progress reports

---

## Project Philosophy

- Clarity beats motivation
- Tracking enables improvement
- Failure data is as valuable as success data
- Small daily actions compound into long-term outcomes

---

## License

This project is currently under active development.  
License details will be added at a later stage.
