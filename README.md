IPL Win Predictor

This Streamlit web application allows you to predict the probability of a team winning an Indian Premier League (IPL) cricket match based on various input parameters. The prediction is made using a machine learning model trained on historical IPL match data.

How to Use

Select Batting Team:
Choose the batting team from the dropdown menu.
Select Bowling Team:
Choose the bowling team from the dropdown menu.
Select Host City:
Select the city where the match is hosted from the dropdown menu.
Enter Target Score:
Input the target score set by the batting team.
Enter Current Score, Overs Completed, and Wickets Out:
Enter the current score, overs completed, and the number of wickets out for the batting team.
Predict Probability:
Click the "Predict Probability" button to calculate and display the predicted win probability for both the batting and bowling teams.
How It Works

The application calculates the win probability based on the following factors:

Runs Left to Chase
Balls Left in the Innings
Wickets in Hand
Current Run Rate (CRR)
Required Run Rate (RRR)
Host City
Batting Team
Bowling Team
The machine learning model takes these input parameters into account and predicts the win probability for both teams. The team with the higher win probability is displayed as the favored team to win the match.

Installation

To run this code locally or modify it, you'll need Python and the following libraries installed:

Streamlit
Pandas
Scikit-learn (sklearn)
You can install these libraries using pip:

bash
Copy code
pip install streamlit pandas scikit-learn
Model

The machine learning model used for prediction is loaded from a pre-trained pickle file (pipe.pkl). The model has been trained on historical IPL match data to make these win probability predictions.

About

This project is a simple IPL win probability predictor created with Streamlit. It demonstrates the use of machine learning for sports analytics and provides an interactive interface for users to make win probability predictions for IPL matches. Feel free to explore the code and customize it for your own use or to improve its accuracy.
