import logging
import joblib
import pandas as pd
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from schemas.student import Student


app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("API started")

logger.info("Loading depression prediction model")

model = joblib.load("model/depression_best_model.pkl")

logger.info("Model loaded successfully")

# Initialising Rate Limiter 
limiter = Limiter(key_func=get_remote_address)


app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)



# Endpoints
@app.get("/")
async def home():
    return {
        "name": "Student Depression Prediction API",
        "message": "API is running",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.get("/about")
async def about():
    return {
        "name": "Student Depression Prediction API",
        "description": "Machine learning API for predicting depression from demographic, academic, lifestyle, and mental-health-related features.",
        "model": "Machine Learning Classification Pipeline",
        "endpoint": "/predict",
        "status": "operational"
    }


@app.post("/predict")
@limiter.limit("20/minute")
async def predict_depression(request: Request, student: Student):
    logger.info("Prediction request received")

    input_data = {
    "Gender": student.Gender,
    "Age": student.Age,
    "City": student.City,
    "Profession": student.Profession,
    "Academic Pressure": student.Academic_Pressure,
    "Work Pressure": student.Work_Pressure,
    "CGPA": student.CGPA,
    "Study Satisfaction": student.Study_Satisfaction,
    "Job Satisfaction": student.Job_Satisfaction,
    "Sleep Duration": student.Sleep_Duration,
    "Dietary Habits": student.Dietary_Habits,
    "Degree": student.Degree,
    "Have you ever had suicidal thoughts ?": student.Suicidal_Thoughts,
    "Work/Study Hours": student.Work_Study_Hours,
    "Financial Stress": student.Financial_Stress,
    "Family History of Mental Illness": student.Family_History_of_Mental_Illness
    }

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    logger.info("Prediction completed")
    result = (
        "Depression predicted"
        if prediction == 1
        else "No depression predicted"
    )

    return {
        "prediction": int(prediction),
        "result": result
    }