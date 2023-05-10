# Salary-Prediction

## Project to Predict the Salary of IT Professionals Based on Certain Inputs


### Introduction
As technology continues to advance and the importance of IT in various industries grows, the demand for skilled IT professionals is on the rise. As a result, there is a growing interest in predicting the salaries of IT professionals based on various factors such as their education, experience, job role, and location. 

In this project, I aim to develop a machine learning model to predict the annual salary of individuals working in the IT industry. By analyzing a large dataset of IT professionals' salaries and their corresponding features, I will train a model to accurately predict salaries based on a given set of input parameters. 

The project will utilize various data processing and modeling techniques to ensure the accuracy and reliability of predictions. The resulting model can be used by IT professionals, recruiters, and employers to gain insights into the factors that influence salaries and to make informed decisions regarding job offers and salary negotiations. Ultimately, this project has the potential to contribute to the development of fair and equitable compensation practices in the IT industry.


### The data
The dataset used was adapted from Stack Overflow Annual Developer Survey. The survey covers an extensive query completed by over 60,000 developers from over 180 countries each year. The data used in this project is from the last 3 years 2020-2022. The dataset and the result from the analysis by Stack Overflow can be found on: https://insights.stackoverflow.com/survey

The revised dataset:
<img width="940" alt="Screenshot 2023-05-10 at 5 59 03 PM" src="https://github.com/juwonlo-tech/salary-prediction/assets/77176412/f826a298-eb51-4456-bbbe-a1fc1d624c18">

The data went through multiple cleaning steps including removal of null values, refining the age values, selecting only full-time IT professionals, cleaning the country values, removing outliers in the salary column, etc.

<img width="940" alt="Screenshot 2023-05-10 at 6 04 52 PM" src="https://github.com/juwonlo-tech/salary-prediction/assets/77176412/783cc0b5-a485-4ea3-a059-9355d373abef">

The categorical data was then passed through the label encoder before the dataset was split into the train and test set in the ratio 70:30.
5 machine learning models were developed to find the best. The GridSearchCV had the least error. GridSearchCV performs an exhaustive search over specified paramenter values for an estimator.

I believe that this project has contributed to the development of fair and equitable compensation practices in the IT industry. By providing a reliable and accurate tool for predicting salaries, I hope to help promote transparency and fairness in the hiring and compensation process.

Overall, the project highlights the power of machine learning and data analysis in solving complex problems and generating valuable insights. As the demand for skilled IT professionals continues to grow, I believe that my model will become an increasingly valuable resource for the industry.

The final model was the packaged and deployed using streamlit to produce a web app with the model in the backend.
<img width="1179" alt="Screenshot 2023-05-10 at 6 27 58 PM" src="https://github.com/juwonlo-tech/salary-prediction/assets/77176412/ce0a6d0d-fec0-4ca1-8417-35525237bb23">
<img width="1179" alt="Screenshot 2023-05-10 at 6 29 09 PM" src="https://github.com/juwonlo-tech/salary-prediction/assets/77176412/102d78bc-7478-4b38-8d87-73db89f32961">

