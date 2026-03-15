import pandas as pd
import matplotlib.pyplot as plt
import statistics

df = pd.read_csv('results.csv')

df['Total Score'] = df[['s1', 's2', 's3', 's4']].sum(axis=1)
df['Total Score(%)'] = df['Total Score'] * 100 / 4
df.rename(columns = {'name': 'Name', 'q1': 'Q1', 'q2': 'Q2', 'q3': 'Q3', 'q4': 'Q4'}, inplace = True)

#df1 to display matrix
df1 = df[['Name', 'Q1', 'Q2', 'Q3', 'Q4', 'Total Score', 'Total Score(%)']]

#results menu
def display_menu():
    print('----Welcome to Quiz Analysis----')
    print('Select an option:')
    print('1. View Quiz Matrix Results')
    print('2. View Statistical Analysis of Marks')
    print('3. View Visualisation of Statistical Analysis')
    print('4. Quit')

def viz_menu():
    print('-----Data Visualisations-----')
    print('Select an option:')
    print('1. View Graph for Total Marks')
    print('2. View Graph for Mean Score')
    print('3. View Graph for Median Score')
    print('4. View Graph for Mode Score')

#display matrix
while True:
    display_menu()
    input1 = input('Please enter your choice (1-4): ')
    if input1 == '1':
        print()
        print(f'Number of participants: {df1['Name'].count()}')
        print()
        print("----------------Quiz Matrix Results----------------")
        print(df1)
        print()

    elif input1 == '2':
        print()
        print("-------Statistical Analysis of Marks-------")
        print('Total Marks Scored per Question:')
        print(f'Q1: {df['s1'].sum()}')
        print(f'Q2: {df['s2'].sum()}')
        print(f'Q3: {df['s3'].sum()}')
        print(f'Q4: {df['s4'].sum()}')
        print(f'Overall: {df['Total Score'].sum()}')
        print('--------------------------')

        max_score = df['Total Score'].max()
        print(f'Highest Score: {max_score}')
        print(f'Highest Score (%): {max_score * 100 /4}')
        print('--------------------------')

        min_score = df['Total Score'].min()
        print(f'Lowest Score: {min_score}')
        print(f'Lowest Score (%): {min_score * 100 /4}')
        print('--------------------------')

        mean_score = df['Total Score'].mean()
        print(f'Mean Score: {mean_score}')
        print(f'Mean Score (%): {mean_score * 100 /4}')
        print('--------------------------')

        median_score = df['Total Score'].median()
        print(f'Median Score: {median_score}')
        print(f'Median Score (%): {median_score * 100 /4}')
        print('--------------------------')

        mode_score = statistics.mode(df['Total Score'])
        print(f'Mode Score: {mode_score}') #to return only mode value without metadata
        print(f'Mode Score (%): {mode_score * 100 /4}')
        print('--------------------------------------------')
        print()

    elif input1 == '3':
        viz_menu()
        input2 = input('Please enter your choice (1-4): ')
        if input2 == '1': #total score graph
            total_score = df['Total Score']
            plt.bar(df['Name'], total_score, color = 'orange', edgecolor ='black')
            plt.xlabel('Participant Name')
            plt.ylabel('Total Score')
            plt.title('Total Score per Participant')
            plt.show()

        if input2 == '2': #mean graph
            mean_score = df[['s1', 's2', 's3', 's4']].mean(axis=1)
            plt.bar(df['Name'], mean_score, color = 'blue', edgecolor ='black')
            plt.xlabel('Participant Name')
            plt.ylabel('Mean Score')
            plt.title('Mean Score per Participant')
            plt.show()

        elif input2 == '3': #median graph
            median_score = df[['s1', 's2', 's3', 's4']].median(axis=1)
            plt.bar(df['Name'], median_score, color ='green', edgecolor ='black')
            plt.xlabel('Participant Name')
            plt.ylabel('Median Score')
            plt.title('Median Score per Participant')
            plt.show()

        elif input2 == '4': #mode graph
            counts = df['Total Score'].value_counts().sort_index()
            counts.plot(kind='bar', color = 'purple', edgecolor = 'black')
            plt.ylabel('Number of participants')
            plt.xlabel('Total Score')
            plt.title('Mode Total Score per Participant')
            plt.xticks(rotation=360, ha='right')
            plt.show()
            plt.show()

    elif input1 == '4':
        print('Exiting program...')
        break

    else:
        print('Please enter a valid option')