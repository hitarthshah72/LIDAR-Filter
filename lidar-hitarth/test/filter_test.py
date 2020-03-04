import unittest
from src.filter import TemporalFilter, RangeFilter


class TemporalRangeTest(unittest.TestCase):

    def test_update(self):
        filter_object = TemporalFilter(n=5, d=3)
        self.assertEqual([0., 1., 2., 1., 3.], filter_object.update(scan=[0, 1, 2, 1, 3]))
        self.assertEqual([0.5, 3, 4.5, 1, 3], filter_object.update(scan=[1, 5, 7, 1, 3]))
        self.assertEqual([1., 3., 4., 1., 3.], filter_object.update(scan=[2, 3, 4, 1, 0]))
        self.assertEqual([1.5, 3., 3.5, 1., 3.], filter_object.update(scan=[3,3,3,1,3]))
        self.assertEqual([2.5, 3., 4., 1., 1.5], filter_object.update(scan=[10, 2, 4, 0, 0]))





if __name__ == "__main__":
    unittest.main()
