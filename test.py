import unittest
import json
from main import app  # Assuming your Flask app instance is named 'app'


class TestRandomFruitEndpoint(unittest.TestCase):

    def setUp(self):
        # Create a test client using the app's test_client method
        self.client = app.test_client()

    def test_random_fruit(self):
        # Send a GET request to the '/random_fruit' endpoint
        response = self.client.get("/")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Decode the response data from JSON
        data = json.loads(response.data.decode("utf-8"))

        # Assert that the 'fruit' key is in the JSON response
        self.assertIn("fruit", data)

        # Assert that the 'fruit' value is one of the predefined FRUITS
        FRUITS = [
            "Apple",
            "Banana",
            "Cherry",
            "Date",
            "Elderberry",
            "Fig",
            "Grape",
            "Honeydew",
            "Imbe",
            "Jackfruit",
            "Kiwi",
            "Lemon",
            "Mango",
            "Nectarine",
            "Orange",
            "Papaya",
            "Quince",
            "Raspberry",
            "Strawberry",
            "Tangerine",
        ]
        self.assertIn(data["fruit"], FRUITS)


if __name__ == "__main__":
    unittest.main()
