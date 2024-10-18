import streamlit as st
from datetime import datetime

if 'tasks' not in st.session_state:
    st.session_state.tasks = 0

now = datetime.now()

def progressPercent(time):
    hour = int(time.strftime('%H')) + 1
    minute = int(time.strftime('%M'))
##    hour, minute = 15, 30
    if hour < 9:
        return 0.0
    elif hour >= 18:
        return 1.0
    else:
        progress = 0
        for i in range(hour-9):
            progress += 0.125
        if hour >= 13:
            progress -= 0.125
        progress += 0.125 * (minute / 60)
        return progress

st.title('Amazing Work Tracker')
st.write('')
st.write('')
st.write('')
taskProgress = st.progress(st.session_state.tasks / 35 if st.session_state.tasks < 35 else 1.0, text=f'Tasks: {st.session_state.tasks}/35')
timeProgress = st.progress(progressPercent(now))

left, centre, right = st.columns(3)

if left.button('', icon=':material/arrow_upward:', use_container_width=True): #task
    st.session_state.tasks += 1
    taskProgress.progress(st.session_state.tasks / 35 if st.session_state.tasks < 35 else 1.0, text=f'Tasks: {st.session_state.tasks}/35')
    timeProgress.progress(progressPercent(now))

if centre.button('', icon=':material/autorenew:', use_container_width=True): #update
    taskProgress.progress(st.session_state.tasks / 35 if st.session_state.tasks < 35 else 1.0, text=f'Tasks: {st.session_state.tasks}/35')
    timeProgress.progress(progressPercent(now))

if right.button('', icon=':material/undo:', use_container_width=True): #reset
    st.session_state.tasks = 0
    taskProgress.progress(st.session_state.tasks / 35 if st.session_state.tasks < 35 else 1.0, text=f'Tasks: {st.session_state.tasks}/35')
    timeProgress.progress(progressPercent(now))


if st.session_state.tasks >= 35:
    st.balloons()


    



