def test_prediction():
    response = client.post("/predict", json=valid_input)

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]