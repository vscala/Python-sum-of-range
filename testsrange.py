import unittest
from srange import srange


class TestSrange(unittest.TestCase):
    def test_no_increment(self):
        for start in range(-100, 100):
            self.assertEqual(srange(start), sum(range(start)))
            for stop in range(-100, 100):
                self.assertEqual(srange(start, stop), sum(range(start, stop)))

    def test_increment(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    if k:
                        self.assertEqual(srange(i, j, k), sum(range(i, j, k)))

    def test_invalid_args(self):
        # Can't pass less than one argument
        with self.assertRaises(TypeError):
            srange()

        # Can't pass more than three arguments
        with self.assertRaises(TypeError):
            srange(1, 2, 3, 4)

        # End argument must be an integer
        with self.assertRaises(TypeError):
            srange(0.1)

        # Can't pass zero increment
        with self.assertRaises(ValueError):
            srange(1, 2, 0)


if __name__ == "__main__":
    unittest.main()
