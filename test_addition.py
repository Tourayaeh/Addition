import addition
import unittest

class TestAddition(unittest.TestCase):
    def test_addition_of_the_int(self):
        self.assertEqual(addition.compute_addition(1,1), 2)

if __name__ == '__main__':
    unittest.main()