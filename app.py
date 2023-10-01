import streamlit as st
import pickle
import pandas as pd

# Define teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select host city', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets],
                             'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.subheader("Predicted Win/Loss Probability")

    # Create a single progress bar with two teams at either side
    progress = st.empty()

    # Calculate the width of the progress bar for win and loss probabilities
    win_width = int(win * 100)
    loss_width = int(loss * 100)

    # Create the HTML code for the progress bar with different colors
    progress_html = f"""
    <div style="display: flex; justify-content: space-between;">
        <div style="background-color: green; width: {win_width}%; height: 20px;"></div>
        <div style="background-color: red; width: {loss_width}%; height: 20px;"></div>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <div style="text-align: center;">
            {batting_team} : {win_width}%
        </div>
        <div style="text-align: center;">
            {bowling_team} : {loss_width}%
        </div>
    </div>
    """

    # Display the custom progress bar
    progress.write(progress_html, unsafe_allow_html=True)
