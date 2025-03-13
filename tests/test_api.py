import pytest
import json
from utils.api_client import ApiClient

# Leer los datos de prueba desde test_data.json
def load_test_data():
    with open("tests/data/test_data.json", "r", encoding="utf-8") as file:
        return json.load(file)["users"]

@pytest.mark.parametrize("payload, expected_status, expected_fields", [
    (user, user["expected_status"], user["expected_fields"]) for user in load_test_data()
])
def test_post_user(payload, expected_status, expected_fields):
    response = ApiClient.create_user(payload)
    assert response.status_code == expected_status, f"Código de estado inesperado: {response.status_code}"
    
    response_json = response.json()
    
    # Verificar que los campos esperados están en la respuesta
    for field in expected_fields:
        assert field in response_json, f"El campo {field} no está en la respuesta"
    
    # Validar que age sea un entero si está presente
    if "age" in response_json:
        assert isinstance(response_json["age"], int), "El campo 'age' no es un entero"
