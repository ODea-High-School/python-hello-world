import unittest
from unittest.mock import patch
from src.main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        with patch('builtins.print') as mock_print:
            hello_world()
            mock_print.assert_called_once_with("Hello, World!")

if __name__ == "__main__":
    unittest.main()
