import unittest

from core import Matrix, Vector


class TestMatrixMulVector(unittest.TestCase):
    def test_square_matrix(self):
        a = Matrix([[1, 2], [3, 4]])
        x = Vector([5, 6])

        result = a.matrix_mul_vector(x)

        self.assertIsInstance(result, Vector)
        self.assertEqual(result.data, [17.0, 39.0])

    def test_rectangular_matrix(self):
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        x = Vector([1, 1, 1])

        result = a.matrix_mul_vector(x)

        self.assertIsInstance(result, Vector)
        self.assertEqual(result.data, [6.0, 15.0])

    def test_empty_matrix(self):
        result = Matrix([]).matrix_mul_vector(Vector([]))

        self.assertIsInstance(result, Vector)
        self.assertEqual(result.data, [])

    def test_dimension_mismatch(self):
        a = Matrix([[1, 2], [3, 4]])
        x = Vector([1, 2, 3])

        with self.assertRaises(ValueError):
            a.matrix_mul_vector(x)


class TestMatrixMulMatrix(unittest.TestCase):
    def test_square_matrix(self):
        a = Matrix([[1, 2], [3, 4]])
        b = Matrix([[5, 6], [7, 8]])

        result = a.matrix_mul_matrix(b)

        self.assertIsInstance(result, Matrix)
        self.assertEqual(result.data, [[19.0, 22.0], [43.0, 50.0]])

    def test_rectangular_matrix(self):
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Matrix([[1, 2], [3, 4], [5, 6]])

        result = a.matrix_mul_matrix(b)

        self.assertIsInstance(result, Matrix)
        self.assertEqual(result.data, [[22.0, 28.0], [49.0, 64.0]])

    def test_empty_matrix(self):
        result = Matrix([]).matrix_mul_matrix(Matrix([]))

        self.assertIsInstance(result, Matrix)
        self.assertEqual(result.data, [])

    def test_dimension_mismatch(self):
        a = Matrix([[1, 2], [3, 4]])
        b = Matrix([[1, 2, 3]])

        with self.assertRaises(ValueError):
            a.matrix_mul_matrix(b)


if __name__ == '__main__':
    unittest.main()
