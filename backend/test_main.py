import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)


class TestDiakriticarAPI(unittest.TestCase):
    @patch('main.httpx.AsyncClient')
    async def test_process_text_success(self, mock_client):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "Doći ću sutra"}

        # Configure mock client
        mock_client_instance = MagicMock()
        mock_client_instance.__aenter__.return_value = mock_client_instance
        mock_client_instance.post.return_value = mock_response
        mock_client.return_value = mock_client_instance

        # Test the API
        response = client.post("/api/process", json={"text": "Doci cu sutra"})

        # Assert response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"processed_text": "Doći ću sutra"})

    def test_empty_text(self):
        response = client.post("/api/process", json={"text": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Text cannot be empty", response.json()["detail"])


if __name__ == "__main__":
    unittest.main()
