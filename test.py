import unittest

from main import fn



class TestFn(unittest.TestCase):
    def test_f5(self):
        # Test with all True inputs
        self.assertTrue(fn(1, 1, 1))
        self.assertTrue(fn(1, 1, 0))
        self.assertTrue(fn(1, 0, 1))
        self.assertTrue(fn(1, 0, 1))



if __name__ == "__main__":
    unittest.main()
