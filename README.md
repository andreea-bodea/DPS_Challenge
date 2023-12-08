# DPS_Challenge
Digital Product School CHALLENGE for Artificial Intelligence Engineer applicants

Dataset: “Monatszahlen Verkehrsunfälle” from the München Open Data Portal (number of accidents for specific categories per month) 

Mission 1: Create an AI Model (code in Jupyter Notebook DPS_Challenge_Mission1.ipynb)
- downloaded the dataset
- visualized historically the number of accidents per category (column1)
  ![Visualization](https://github.com/andreea-bodea/DPS_Challenge/assets/58235076/ea3ba670-8591-40aa-a1a0-745ab7f69ffc)

- created an application that forecasts the values for:
Category: 'Alkoholunfälle'
Type: 'insgesamt'
Year: '2021'
Month: '01'
using Linear Regression
- tested the prediction model and visualized the results
  ![Prediction](https://github.com/andreea-bodea/DPS_Challenge/assets/58235076/d232d18d-feb0-4f9d-bc7e-155035a41f79)



Mission 2: Publish your source code & deploy
- published source code in GitHub repository (both the code with comments and the visualization itself as an image)
- deployed the model (converted to a Flask application) to Render as cloud service
- createed an endpoint that returns the predictions that accepts a POST request with a JSON body in the follosing format: 
{
"year":2020,
"month":10
}
and returns the applications prediction in the following format: 
{
"prediction":value
}

Mission 3: Send the URL of the work
- made a POST request to the URL https://dps-challenge.netlify.app/.netlify/functions/api/challenge
Body: 
{
"github":"https://github.com/ACCOUNT/REPO",
"email":"EMAIL",
"url":"DEPLOYED_ENDPOINT", 
"notes":"NOTES"
}
