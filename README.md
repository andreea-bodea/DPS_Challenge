# DPS_Challenge
Digital Product School CHALLENGE for Artificial Intelligence Engineer applicants

Dataset: “Monatszahlen Verkehrsunfälle” from the München Open Data Portal (number of accidents for specific categories per month) 

Mission 1: Create an AI Model
- download the dataset
- visualize historically the number of accidents per category (column1)
- create an application that forecasts the values for:
Category: 'Alkoholunfälle'
Type: 'insgesamt'
Year: '2021'
Month: '01'
- compute the error between your prediction values and the actual numbers (ground truth data)

Mission 2: Publish your source code & Deploy
- publish source code in a github repository (both the code with comments and the visualisation itself as an image)
- deploy the model. You would need to create an endpoint that returns your predictions. Make sure that your endpoint accepts a POST request with a JSON body like this: 
{
"year":2020,
"month":10
}

And it should return your applications prediction in the following format:
 
{
"prediction":value
}

The model can be deployed to a cloud service. You can use (aws, google cloud, heroku or whatever you prefer, they usually all provide a freetier)

Mission 3: Send us the URL of your work
- make a POST request to the following URL https://dps-challenge.netlify.app/.netlify/functions/api/challenge
Body: 
{
"github":"https://github.com/ACCOUNT/REPO",
"email":"EMAIL",
"url":"DEPLOYED_ENDPOINT", 
"notes":"NOTES" // Not mandatory
}
Fill in your email address for EMAIL, the path to your github repo at ACCOUNT/REPO and the link of your deployed model at DEPLOYED_ENDPOINT.
Content type
The Content-Type of the request must be application/json.

Sample Request
POST https://dps-challenge.netlify.app/.netlify/functions/api/challenge
Content-Type: application/json 

{
"github":"https://github.com/DigitalProductschool/website",
"email":"name@example.com",
"url":"https://digitalproductschool.io/", 
"notes":"I deployed using ..." // Not mandatory
}
Sample Response
If your POST request succeeds, the server returns HTTP status code 200.

Status 200 OK 
{"message":"Congratulations! Achieved Mission 3"}



