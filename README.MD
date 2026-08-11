# Student Depression Prediction API

A machine learning project for predicting depression from demographic, academic, lifestyle, and mental-health-related features. The project covers the complete workflow from data exploration and preprocessing to model evaluation and deployment through a FastAPI REST API.

## Project Overview

The model uses student-related features such as age, academic pressure, work pressure, CGPA, sleep duration, study satisfaction, financial stress, family history of mental illness, and other demographic and lifestyle factors to predict whether depression is present.

The machine learning workflow includes:

* Exploratory data analysis
* Data cleaning and validation
* Missing-value handling
* Categorical and ordinal feature encoding
* Numerical feature scaling
* Train/test splitting
* Cross-validation
* Hyperparameter optimization
* Classification model comparison
* Model evaluation using accuracy, precision, recall, and F1-score
* Serialization of the complete preprocessing and prediction pipeline
* Deployment through a FastAPI REST API

## Machine Learning Pipeline

The preprocessing pipeline handles different feature types independently:

* **Numerical features:** median imputation followed by standardization
* **Categorical features:** one-hot encoding with unknown-category handling
* **Ordinal features:** ordinal encoding with explicitly defined category ordering
* **Binary features:** one-hot encoding

The preprocessing steps are included in the saved model pipeline, allowing the API to receive raw feature values without requiring the client to reproduce the training preprocessing.

## Features

The model uses the following input features:

| Feature                          | Type        |
| -------------------------------- | ----------- |
| Gender                           | Categorical |
| Age                              | Numerical   |
| City                             | Categorical |
| Profession                       | Categorical |
| Academic Pressure                | Numerical   |
| Work Pressure                    | Numerical   |
| CGPA                             | Numerical   |
| Study Satisfaction               | Numerical   |
| Job Satisfaction                 | Numerical   |
| Sleep Duration                   | Ordinal     |
| Dietary Habits                   | Categorical |
| Degree                           | Categorical |
| Suicidal Thoughts                | Categorical |
| Work/Study Hours                 | Numerical   |
| Financial Stress                 | Numerical   |
| Family History of Mental Illness | Categorical |

The target variable is **Depression**.

## API

The trained model is served using **FastAPI**.

### Endpoints

#### `GET /`

Returns basic information about the API and available endpoints.

#### `GET /about`

Returns information about the prediction system and underlying model.

#### `GET /health`

Returns the operational status of the API and verifies that the model has been loaded.

#### `POST /predict`

Accepts student information and returns a depression prediction.

Example response:

```json
{
  "prediction": 1,
  "result": "Depression predicted"
}
```

The API also performs input validation using Pydantic.

## Running Locally

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is automatically available at:

```text
http://127.0.0.1:8000/docs
```

## Model

The trained model is serialized using `joblib`. The saved object contains the complete machine learning pipeline, including preprocessing and the final classifier.

```python
import joblib

model = joblib.load("depression_best_model.pkl")
```

Predictions can then be generated directly from a dataframe containing the raw input features:

```python
prediction = model.predict(input_data)
```

## Engineering Features

The API includes several features intended to make the model suitable for practical deployment:

* FastAPI-based model serving
* Pydantic request validation
* Structured application logging
* Rate limiting
* Health monitoring endpoint
* Automated API/model tests
* Serialized model pipeline
* Interactive OpenAPI documentation

## Notebook

The complete machine learning development and experimentation process is available in Google Colab:

[Open the Google Colab notebook](https://colab.research.google.com/drive/1Chh7vMBBw5U3j-a26JWyjlJzkgfvVRyV?usp=sharing&utm_source=chatgpt.com)

## Project Structure

```
depression-prediction-api/
│
├── main.py
├── requirements.txt
├── README.md
│
├── model/
│   └── depression_best_model.pkl
│
├── schemas/
│   └── student.py
│
└── tests/
    └── test_prediction.py
```

## Disclaimer

This project is an educational and engineering demonstration of machine learning applied to depression prediction. The model is **not a medical diagnostic system** and should not be used to diagnose, treat, or make clinical decisions about an individual.

Predictions reflect patterns learned from the training dataset and should not be interpreted as clinical assessments.
