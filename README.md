# RESTAURANT REVENUE PREDICTION
<img src="images/restaurant-img.jpg" alt="Example Image" width="1000" height="350"/>

## Introduction
<a name="introduction"></a>
The "Restaurant Revenue Prediction" project aims to build a predictive model to forecast the revenue of restaurants based on a variety of features such as number of customers, type of cuisine, reviews, menu price etc. This project leverages advanced machine learning techniques and data analytics to provide actionable insights that can help restaurant owners and managers make informed decisions to optimize their revenue streams.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)
10. [Acknowledgements](#acknowledgements)

## Features
<a name="features"></a>
The project is meant to deliver the following:
1. **Revenue Prediction**: Utilizes advanced machine learning models to predict future revenues with high accuracy, helping restaurant owners forecast their earnings effectively.
2. **Comprehensive Data Analysis**: Analyzes a wide range of factors that impact restaurant revenues, including historical sales data, location demographics, customer reviews, and market trends.
3. **Key Revenue Drivers Identification**: Identifies the most influential factors that drive revenue, providing valuable insights into what contributes most to a restaurant's success.
4. **User-Friendly Interface**: Features a user-friendly interface for easy interaction with the model, allowing users to input data and receive predictions without needing extensive technical knowledge.

## Getting Started
<a name="getting-started"></a>
The project includes a Flask application implemented in `application.py`. It can be run using code editors such as VSCode. The server will be hosted locally, and the web application can be accessed by opening the browser and navigating to http://localhost:5000. To launch the web application, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yc1909/Restaurant-Revenue-Prediction.git

# Navigate to the project directory
cd Restaurant-Revenue-Prediction

# Install the required dependencies
pip install -r requirements.txt

# Run the application
python application.py
```

## Usage
<a name="usage"></a>
### Data Preparation

Collect and preprocess your data:
1. **Data Collection**: Gather historical sales, customer reviews, location demographics, and market trends. The dataset in this project is acquired from: https://www.kaggle.com/datasets/mrsimple07/restaurants-revenue-prediction/data
2. **Data Cleaning**: Handle missing values, remove duplicates, and correct inconsistencies.
3. **Data Preprocessing**: Encode categorical variables, normalize numerical variables, and create new features.

### Model Training
Train the machine learning model using the prepared dataset.
<img src="images/model-func.png" alt="model function" width="500" height="500"/>
<img src="images/model-trainer.png" alt="model trainer" width="500" height="500"/>

### Generating Predictions
Use the trained model to generate revenue predictions.
<img src="images/predictions.png" alt="predictions" width="500" height="500"/>

### Visualization and Analysis
Visualize data and predictions to analyze results.
<img src="images/viz-analysis.png" alt="analysis" width="500" height="500"/>






