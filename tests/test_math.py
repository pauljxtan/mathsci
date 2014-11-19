import math
import unittest

from mathsci.datatypes import Vector, Matrix
from mathsci.math import chaos, derivative, discrete, linalg, lineq, maxmin

class TestMath(unittest.TestCase):

    def test_chaos_lorenz_attractor(self):
        t = 0.1
        x = 2.3; y = 4.5; z = 6.7
        sigma = 8.9; beta = 0.1; rho = 2.3

        self.assertEqual(chaos.lorenz_attractor(t, [x, y, z], sigma=sigma,
                                                beta=beta, rho=rho),
                         Vector([sigma * (y - x), x * (rho - z) - y,
                          x * y - beta * z]))

    def test_derivative(self):
        f = lambda x: 2 * x**3;
        fp = lambda x: 6 * x**2
        x = 4

        self.assertTrue(abs(derivative.forward_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.backward_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.central_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.central_difference_second(f, x, 1e-3) - fp(x)) < 1e-6)

    def test_discrete(self):
        self.assertEqual(discrete.factorial(7), 5040)
        self.assertEqual(discrete.binomial_coefficient(7, 3), 35)

    def test_linalg(self):
        A = [1, 3, 2, 4, 3, 5]
        B = [1, 2, 4, 7, 11, 16]
        C = Matrix([[5, 2, 7, 4],
                    [2, 7, 5, 9],
                    [7, 2, 3, 6],
                    [3, 7, 1, 8]])

        self.assertEqual(linalg.dot_product(A, B), 156)
        self.assertEqual(linalg.determinant_minors(C), 488)

    def test_lineq(self):
        A = Matrix([[2.0,  1.0,  4.0,  1.0],
                    [3.0,  4.0, -1.0, -1.0],
                    [1.0, -4.0,  1.0,  5.0],
                    [2.0, -2.0,  1.0,  3.0]])
        b = [-4, 3, 9, 7]
        
        x = lineq.gauss_elim(A, b)
        self.assertTrue(abs(x[0] -  2.0) < 1e-9)
        self.assertTrue(abs(x[1] - -1.0) < 1e-9)
        self.assertTrue(abs(x[2] - -2.0) < 1e-9)
        self.assertTrue(abs(x[3] -  1.0) < 1e-9)

    def test_maxmin(self):
        f1 = lambda x: (x - 3)**2
        f2 = lambda x: -(x - 3)**2

        self.assertTrue(abs(maxmin.golden_ratio_min(f1, -100, 100, 1e-6)[0]
                            - 3) < 1e-7)
        self.assertTrue(abs(maxmin.golden_ratio_max(f2, -100, 100, 1e-6)[0]
                            - 3) < 1e-7)

if __name__ == '__main__':
    unittest.main()