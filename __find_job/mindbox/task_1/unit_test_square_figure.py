import unittest
from __find_job.task_1 import square_figure


class TestSquareFigure(unittest.TestCase):

    def setUp(self):
        self.square = square_figure.SquareFigure()


    def test_circle(self):
        self.assertEqual(self.square.circle(5), 78.54)


    def test_triangle(self):
        self.assertEqual(self.square.triangle(25, 24, 7), (84.0, 'является прямоугольным'))


    def test_unknown_figure(self):
        self.assertEqual(self.square.unknown_figure(5), 'Площадь окружности 78.54')


if __name__ == '__main__':
    unittest.main()
