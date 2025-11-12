from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    """Verifica que el endpoint de salud responda correctamente."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_product():
    """Prueba la creación de un producto."""
    data = {"name": "Teclado", "price": 2500,
            "description": "Teclado mecánico"}
    response = client.post("/products/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Teclado"
    assert "id" in response.json()


def test_get_products():
    """Prueba la obtención de productos."""
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
