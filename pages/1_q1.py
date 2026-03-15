import streamlit as st

st.write('1/4')
st.write('Name:', st.session_state['name']) #display participant's name

st.title('QUESTION 1')
st.text('Which Malaysian state is considered the rice bowl of the country?')
q1_choice = st.radio('Select one option', ['A. Johor', 'B. Kedah', 'C. Penang', 'D. Selangor'])
if st.button("Submit"): #marks the answer wrong or correct
    if q1_choice == 'B. Kedah':
        st.success('Correct Answer')
        st.session_state['score1'] = 1
        st.session_state['answer1'] = 'B'

    elif q1_choice == 'A. Johor':
        st.error('Wrong Answer')
        st.session_state['score1'] = 0
        st.session_state['answer1'] = 'A'

    elif q1_choice == 'C. Penang':
        st.error('Wrong Answer')
        st.session_state['score1'] = 0
        st.session_state['answer1'] = 'C'

    elif q1_choice == 'D. Selangor':
        st.error('Wrong Answer')
        st.session_state['score1'] = 0
        st.session_state['answer1'] = 'D'

#navigation buttons
if st.button('Next'):
    st.switch_page('pages/2_q2.py')
if st.button('Back to Main'):
    st.switch_page('main.py')