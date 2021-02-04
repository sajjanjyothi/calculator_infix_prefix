import unittest
from kheiron_rest_server import app

class TestRestServer(unittest.TestCase):
    def test_rest_server(self):
        app_client = app.test_client()
        self.assertEqual(-1.8,app_client.post('/kheiron/api/v1/calculator',json={"expression":"( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"}).get_json()['result'])
        self.assertEqual(3,app_client.post('/kheiron/api/v1/calculator',json={"expression":"- / 10 + 1 1 * 1 2"}).get_json()['result'])


if __name__ == '__main__':
    unittest.main()
