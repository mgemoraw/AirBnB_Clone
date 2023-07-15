from base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        base = BaseModel()
        self.assertEqual(base.id, None)


if __name__ == "__main__":
    unittest.main()
