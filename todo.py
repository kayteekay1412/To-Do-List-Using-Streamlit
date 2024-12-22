# -*- coding: utf-8 -*-
"""
@author: ktk
"""

import streamlit as st

st.title("To Do List")

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

task = st.text_input("Enter your task", "")

if st.button("Add Task"):
    if task.strip():
        st.session_state["task_list"].append(task.strip())
    else:
        st.warning("Task cannot be empty.")

st.subheader("Your Tasks")
for i, t in enumerate(st.session_state["task_list"]):
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.write(f"{i + 1}) {t}")
    with col2:
        if st.checkbox("Done", key=f"task_{i}"):
            st.session_state["task_list"].pop(i)
            st.experimental_rerun()
