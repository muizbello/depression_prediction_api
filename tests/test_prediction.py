from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


valid_input = {
    "Gender": "Male",
    "Age": 21,
    "City": "Mumbai",
    "Profession": "Student",
    "Academic_Pressure": 3.0,
    "Work_Pressure": 2.0,
    "CGPA": 8.5,
    "Study_Satisfaction": 3.0,
    "Job_Satisfaction": 3.0,
    "Sleep_Duration": "7-8 hours",
    "Dietary_Habits": "Healthy",
    "Degree": "B.Tech",
    "Suicidal_Thoughts": "No",
    "Work_Study_Hours": 6.0,
    "Financial_Stress": 2.0,
    "Family_History_of_Mental_Illness": "No"
}


def test_prediction():
    response = client.post("/predict", json=valid_input)

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert data["prediction"] in [0, 1]