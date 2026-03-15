import streamlit as st

#initialise name variable

st.title('Welcome to the Malaysian Food Quiz 🍛 🍜')
st.text('Embark on this quiz and test your knowledge on Malaysian food!')

#allows user to enter name
if 'name' not in st.session_state:
    st.session_state['name'] = ''
st.session_state['name'] = st.text_input(
    'Please enter your name: ',
    value=st.session_state['name']
)

if st.button("Start Quiz"):
    st.switch_page('pages/1_q1.py') #move to question 1

#initialise session states - scores
if 'score1' not in st.session_state:
    st.session_state['score1'] = 0

if 'score2' not in st.session_state:
    st.session_state['score2'] = 0

if 'score3' not in st.session_state:
    st.session_state['score3'] = 0

if 'score4' not in st.session_state:
    st.session_state['score4'] = 0

#initialise session states - answers (e.g. A, B, C, D)
if 'answer1' not in st.session_state:
    st.session_state['answer1'] = ''

if 'answer2' not in st.session_state:
    st.session_state['answer2'] = ''

if 'answer3' not in st.session_state:
    st.session_state['answer3'] = ''

if 'answer4' not in st.session_state:
    st.session_state['answer4'] = ''