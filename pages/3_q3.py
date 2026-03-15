import streamlit as st
from PIL import Image

#Question page - 3
st.write('3/4')
st.write('Name:', st.session_state['name']) #display participant's name

st.title('QUESTION 3')
st.text('Name the dish in this image')
img3 = Image.open('roti.png')
st.image(img3, width=400)
q3_choice = st.radio('Select one option', ['A. Roti canai', 'B. Nasi lemak', 'C. Char kway teow', 'D. Nasi kandar'])
if st.button("Submit"):
    if q3_choice == 'A. Roti canai':
        st.success('Correct Answer')
        st.session_state['score3'] = 1
        st.session_state['answer3'] = 'A'

    elif q3_choice == 'B. Nasi lemak':
        st.error('Wrong Answer')
        st.session_state['score3'] = 0
        st.session_state['answer3'] = 'B'

    elif q3_choice == 'C. Char kway teow':
        st.error('Wrong Answer')
        st.session_state['score3'] = 0
        st.session_state['answer3'] = 'C'

    elif q3_choice == 'D. Nasi kandar':
        st.error('Wrong Answer')
        st.session_state['score3'] = 0
        st.session_state['answer3'] = 'D'

if st.button("Next"):
    st.switch_page('pages/4_q4.py')
if st.button('Previous'):
    st.switch_page('pages/2_q2.py')