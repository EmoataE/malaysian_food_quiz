import streamlit as st
from PIL import Image
import pandas as pd
import os

player_list = [] #to store player once quiz is complete

class Player: #template to record participant's answers and marks
    def __init__(self, name, q1:str, q2:str, q3:str, q4:str, s1:int, s2:int, s3:str, s4:str):
        self.name = name
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

#Question page - 4
st.write('4/4')
st.write('Name:', st.session_state['name']) #display participant's name

st.title('QUESTION 4')
st.text('Where did this dish, chilli pan mee originate from?')
img4 = Image.open('pages/mee.png')
st.image(img4, width=400)
q4_choice = st.radio('Select one option', ['A. Johor Bahru', 'B. Kuala Lumpur', 'C. Ipoh', 'D. Melaka City'])
if st.button("Submit"):
    if q4_choice == 'B. Kuala Lumpur':
        st.success('Correct Answer')
        st.session_state['score4'] = 1
        st.session_state['answer4'] = 'B'

    elif q4_choice == 'A. Johor Bahru':
        st.error('Wrong Answer')
        st.session_state['score4'] = 0
        st.session_state['answer4'] = 'A'

    elif q4_choice == 'C. Ipoh':
        st.error('Wrong Answer')
        st.session_state['score4'] = 0
        st.session_state['answer4'] = 'C'

    elif q4_choice == 'D. Melaka City':
        st.error('Wrong Answer')
        st.session_state['score4'] = 0
        st.session_state['answer4'] = 'D'

st.write('Click "End Quiz" to see your results!')

if st.button('End Quiz'): #save player's scores after they click 'End Quiz'
    a = st.session_state['answer1']
    b = st.session_state['answer2']
    c = st.session_state['answer3']
    d = st.session_state['answer4']
    e = st.session_state['score1']
    f = st.session_state['score2']
    g = st.session_state['score3']
    h = st.session_state['score4']
    add_player = Player(st.session_state['name'], a, b, c, d, e, f, g, h)
    player_list.append(add_player)

    #save player's name and answers into external csv
    directory = 'C:/Users/User/PyCharmMiscProject/pp_ass2'
    filename = 'results.csv'

    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, filename)
    new_data = pd.DataFrame([vars(add_player) for add_player in player_list])
    new_data.to_csv(file_path, mode = 'a', index=False, header = not os.path.exists(file_path))

    st.success('Results saved!')
    st.switch_page('pages/5_result.py')

if st.button('Previous'):
    st.switch_page('pages/3_q3.py')
