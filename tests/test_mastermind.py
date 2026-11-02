# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from play import feedback, new_secret, validate_guess

class MastermindTests(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(feedback("1234", "1234"), (4, 0))
    def test_misplaced(self):
        self.assertEqual(feedback("1234", "4321"), (0, 4))
    def test_duplicates(self):
        self.assertEqual(feedback("1122", "1211"), (2, 1))
    def test_invalid(self):
        for guess in ("123", "12345", "1294", "abcd"):
            with self.assertRaises(ValueError):
                validate_guess(guess)
    def test_generated_secret(self):
        self.assertEqual(len(validate_guess(new_secret())), 4)

if __name__ == "__main__":
    unittest.main()
