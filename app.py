import streamlit as st

st.title("🚀 My Peace & Impact Planner")

# User Inputs
task = st.text_input("What's the task?")
impact = st.slider("Future Impact (0-10)", 0, 10, 5)
peace = st.slider("Mental Peace (0-10)", 0, 10, 5)

if st.button("Calculate Priority"):
    score = (impact * 0.6) + (peace * 0.4)
    if score > 7:
        st.success(f"DO THIS NOW: {task}")
    elif score > 4:
        st.warning(f"PLAN THIS: {task}")
    else:
        st.info(f"IGNORE THIS: {task}")
      
