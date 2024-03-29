import unittest
from IBITNormalizer.normalizer import IBITNormalizer


class TestNormalizer(unittest.TestCase):

    def test_normalize_text(self):
        self.assertEqual(IBITNormalizer.forLM().normalize('سلام'), 'سلام')
        self.assertEqual(IBITNormalizer.forLLM().normalize('سلام'), 'سلام')


if __name__ == '__main__':
    unittest.main()
