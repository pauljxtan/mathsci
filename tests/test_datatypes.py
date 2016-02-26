import unittest

from mathsci.datatypes import Vector, Matrix

# TODO: use epsilon error testing for float comparisons?

class TestDatatypes(unittest.TestCase):

    def test_Vector(self):
        x = Vector([1.0, 2.0, 3.0])
        y = Vector([4.0, 5.0, 6.0])
        z = Vector([3.0, 2.0, 1.0])
        w = Vector([-1.2, 3.4, -5.6])

        # Representations
        self.assertEqual(str(x), "[1.0 2.0 3.0]")

        # Container methods
        self.assertEqual(y[1], 5.0)

        # Unary operators
        self.assertEqual(+w, Vector([+(-1.2), +3.4, +(-5.6)]))
        self.assertEqual(-w, Vector([-(-1.2), -3.4, -(-5.6)]))
        self.assertEqual(abs(w), Vector([1.2, 3.4, 5.6]))

        # Element-wise comparisons
        self.assertEqual(x < z, Vector([True, False, False]))
        self.assertEqual(x > z, Vector([False, False, True]))
        self.assertEqual(x <= z, Vector([True, True, False]))
        self.assertEqual(x >= z, Vector([False, True, True]))

        # Element-wise arithmetic
        self.assertEqual(x + y, Vector([5.0, 7.0, 9.0]))
        self.assertEqual(x - y, Vector([-3.0, -3.0, -3.0]))
        self.assertEqual(x * y, Vector([4.0, 10.0, 18.0]))
        self.assertEqual(x / y, Vector([0.25, 0.4, 0.5]))

        # Scalar arithmetic
        self.assertEqual(x.add_scalar(4.0), Vector([5.0, 6.0, 7.0]))
        self.assertEqual(x.sub_scalar(4.0), Vector([-3.0, -2.0, -1.0]))
        self.assertEqual(x.mul_scalar(4.0), Vector([4.0, 8.0, 12.0]))
        self.assertEqual(x.div_scalar(4.0), Vector([0.25, 0.5, 0.75]))

        # Vector operations
        self.assertEqual(x.dot_product(y), 32.0)

        # Adding/removing elements
        x.append(4.0)
        self.assertEqual(x, Vector([1.0, 2.0, 3.0, 4.0]))
        y.prepend(7.0)
        self.assertEqual(y, Vector([7.0, 4.0, 5.0, 6.0]))
        x.insert(2, 5.0)
        self.assertEqual(x, Vector([1.0, 2.0, 5.0, 3.0, 4.0]))
        y.remove(1)
        self.assertEqual(y, Vector([7.0, 5.0, 6.0]))

    def test_Matrix(self):
        x = Matrix([[1.0, 2.0, 3.0],
                    [4.0, 5.0, 6.0],
                    [7.0, 8.0, 9.0]])
        y = Matrix([[1.0, 3.0, 2.0],
                    [4.0, 3.0, 5.0],
                    [4.0, 6.0, 5.0]])
        w = Matrix([[1.2, -3.4], [5.6, -7.8]])
        
        # Representations
        self.assertEqual(str(x), "[[1.0 2.0 3.0]\n"
                                 " [4.0 5.0 6.0]\n"
                                 " [7.0 8.0 9.0]]")

        # Unary operators
        #self.assertEqual(+w, Matrix([[+1.2, +(-3.4)], [+5.6, +(-7.8)]]))
        #self.assertEqual(-w, Matrix([[-1.2, -(-3.4)], [-5.6, -(-7.8)]]))
        #self.assertEqual(abs(w), Matrix([[1.2, 3.4], [5.6, 7.8]]))

        # Element-wise arithmetic
        self.assertEqual(x + y, Matrix([[2.0, 5.0, 5.0],
                                        [8.0, 8.0, 11.0],
                                        [11.0, 14.0, 14.0]]))
        self.assertEqual(x - y, Matrix([[0.0, -1.0, 1.0],
                                        [0.0, 2.0, 1.0],
                                        [3.0, 2.0, 4.0]]))
        self.assertEqual(x * y, Matrix([[1.0, 6.0, 6.0],
                                        [16.0, 15.0, 30.0],
                                        [28.0, 48.0, 45.0]]))

        # Matrix operations
        self.assertEqual(x.mul_matrix(y), Matrix([[21.0, 27.0, 27.0],
                                                  [48.0, 63.0, 63.0],
                                                  [75.0, 99.0, 99.0]]))

        # Adding/removing elements
        x.append_row([1.2, 3.4, 5.6])
        self.assertEqual(x, Matrix([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0],
                                    [7.0, 8.0, 9.0],
                                    [1.2, 3.4, 5.6]]))
        y.append_col([9.8, 7.6, 5.4])
        self.assertEqual(y, Matrix([[1.0, 3.0, 2.0, 9.8],
                                    [4.0, 3.0, 5.0, 7.6],
                                    [4.0, 6.0, 5.0, 5.4]]))


if __name__ == '__main__':
    unittest.main(verbosity=2)