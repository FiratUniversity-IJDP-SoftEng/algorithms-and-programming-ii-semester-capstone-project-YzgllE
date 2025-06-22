import unittest
from algorithm import rabin_karp

class TestRabinKarp(unittest.TestCase):
    def test_match(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABABC"
        matches, _ = rabin_karp(text, pattern)
        self.assertEqual(matches, [10])

    def test_no_match(self):
        text = "ABCDEFG"
        pattern = "HIJ"
        matches, _ = rabin_karp(text, pattern)
        self.assertEqual(matches, [])

if __name__ == '__main__':
    unittest.main()
