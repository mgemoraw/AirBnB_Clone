from my_math.abs import abs
import unittest


class TestAbs(unittest.TestCase):
    def test_abs(self):
        result = abs(-3)
        self.assertEqual(result, 3)
        self.assertEqual(abs(1), 1)
        self.assertEqual(abs(-98), 98)

    def test_error(self):

        # self.assertRaises(ValueError, abs, "f")
        with self.assertRaises(ValueError):
            abs("f")


if __name__ == "__main__":
    unittest.main()
