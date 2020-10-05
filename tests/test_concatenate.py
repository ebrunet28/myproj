import unittest
from numpy.testing import assert_array_equal

import numpy as np

from myproj.concatenate import Concatenation


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._a1 = np.array(['a', 'b'])
        self._a2 = np.array(['E', 'F'])

    def tearDown(self) -> None:
        pass


class TestConcatenation(BaseTestCase):
    def test_concatenate(self):
        concatenation = Concatenation(
            a1=self._a1,
            a2=self._a2,
        )
        result = concatenation.concatenate()
        assert_array_equal(
            result,
            np.array(['aE', 'bF'])
        )
