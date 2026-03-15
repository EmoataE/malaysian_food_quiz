import streamlit as st
import pandas as pd

#to display answers (e.g. A, B, C or D)
a1 = st.session_state['answer1']
a2 = st.session_state['answer2']
a3 = st.session_state['answer3']
a4 = st.session_state['answer4']

#calculation of results
q1 = st.session_state['score1']
q2 = st.session_state['score2']
q3 = st.session_state['score3']
q4 = st.session_state['score4']
result = q1 + q2 + q3 + q4

#result summary table
data = {
    'Question': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Answer': [a1, a2, a3, a4],
    'Score': [q1, q2, q3, q4]
}

df = pd.DataFrame(data)

#show results here
st.header('Your Results:')
if st.session_state['name']:
    st.write('Name:', st.session_state['name'])
st.write('Total Score (out of 4):', result)
st.divider()
st.header('Results Summary')
st.table(df)
if st.button('Quit'):
    st.switch_page('pages/6_exit.py')
