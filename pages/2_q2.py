import streamlit as st

#Question page -2
st.write('2/4')
st.write('Name:', st.session_state['name']) #display participant's name

st.title('QUESTION 2')
st.text('Which of the following is a popular hot milk tea beverage found in Malaysia?')
q2_choice = st.radio('Select one option', ['A. Pepsi', 'B. Teh Tarik', 'C. Matcha', 'D. Air bandung'])
if st.button("Submit"):
    if q2_choice == 'B. Teh Tarik':
        st.success('Correct Answer')
        st.session_state['score2'] = 1
        st.session_state['answer2'] = 'B'

    elif q2_choice == 'A. Pepsi':
        st.error('Wrong Answer')
        st.session_state['score2'] = 0
        st.session_state['answer2'] = 'A'

    elif q2_choice == 'C. Matcha':
        st.error('Wrong Answer')
        st.session_state['score2'] = 0
        st.session_state['answer2'] = 'C'

    elif q2_choice == 'D. Air bandung':
        st.error('Wrong Answer')
        st.session_state['score2'] = 0
        st.session_state['answer2'] = 'D'

if st.button('Next'):
    st.switch_page('pages/3_q3.py')
if st.button('Previous'):
    st.switch_page('pages/1_q1.py')