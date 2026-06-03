from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"App Running" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["service"] == "flask-api"
    assert data["version"] == "1.0"


def test_predict():
    client = app.test_client()

    response = client.get("/predict")

    assert response.status_code == 200

    data = response.get_json()

    assert data["prediction"] == "coming soon"