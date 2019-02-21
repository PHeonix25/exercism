import unittest

from prime_factors import prime_factors


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class PrimeFactorsTest(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesWithMessage(ValueError):
            prime_factors(-1)
    
    def test_zero(self):
        with self.assertRaisesWithMessage(ValueError):
            prime_factors(0)

    def test_no_factors(self):
        self.assertEqual(prime_factors(1), [])

    def test_prime_number(self):
        self.assertEqual(prime_factors(2), [2])

    def test_square_of_a_prime(self):
        self.assertEqual(prime_factors(9), [3, 3])

    def test_cube_of_a_prime(self):
        self.assertEqual(prime_factors(8), [2, 2, 2])

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])

    def test_product_of_primes(self):
        self.assertEqual(prime_factors(901255), [5, 17, 23, 461])

    def test_factors_include_a_large_prime(self):
        self.assertEqual(prime_factors(93819012551), [11, 9539, 894119])

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

if __name__ == '__main__':
    unittest.main()
