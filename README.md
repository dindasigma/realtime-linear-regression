# Realtime Simple Linear Regression with Scikit-learn, Flask, and React

Realtime simple linear regression with Scikit-learn, Flask, and React to predict the amount of memory that will need after the next three months. For creating the web application, I used Flask for backend and ReactJS for frontend. Data gather time to time using WHMCS API and model retrain using Scikit-learn. The result of data prediction sends to client-side using Flask. In the client-side, visualization done with Uber’s React-vis library.

## TODO List

**Backend (Scikit-learn, Flask)**
1. Cron job to get new data (get_data.py) [done!]
2. Cron job to retrain model (retrain.py) [done!]
3. API for sending real and predicted data [todo]

**Frontend (React)**
1. Visualize data [todo]
2. Visualize regression line and predicted data [todo]


## Running Environment

- python 3.6
- scikit-learn 0.20
- flask 1.1


## Data
For this demo, I use dummy data includes days and the amount of memory needed. 
Example data:

| day | memory |
| --- | --- |
| 0 | 0 |
| 1 | 15 |
| 2 | 55 |
| 3 | 94 |
| 4 | 130 |
| 5 | 137 |
| 6 | 141 |
| 7 | 151 |