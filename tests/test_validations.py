from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_product_invalid_price():
    """Debe rechazar precios negativos."""
    response = client.post(
        "/products/", json={"name": "Producto inválido", "price": -1}
    )
    assert response.status_code == 422
