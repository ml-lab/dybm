# -*- coding: utf-8 -*-

__author__ = "Takayuki Osogami"
__copyright__ = "(C) Copyright IBM Corp. 2016"

import unittest
import numpy as np
from six.moves import xrange

import tests.simple
from tests.arraymath import NumpyTestMixin, CupyTestMixin
from pydybm.time_series.esn import ESN
from pydybm.base.sgd import AdaGrad


class ESNTestCase(object):
    """
    unit test for ESN
    """

    def setUp(self):
        # learning rate
        self.rate = 0.1
        self.esn_dim = 4

    def tearDown(self):
        pass

    def testGenerative(self):
        """
        testing minimal consistency in learning a sequence
        """
        print("VectorRegressionTestCase.testGenerative")
        in_dim = 3     # dimension of input sequence
        max_repeat = 100000
        for SGD in [AdaGrad]:
            print("SGD:")
            print(SGD)
            model = ESN(self.esn_dim, in_dim, in_dim)
            model.set_learning_rate(self.rate)
            i = tests.simple.test_real_model(model, max_repeat)
            self.assertLess(i, max_repeat)

    def testDiscriminative(self):
        print("VectorRegressionTestCase.testDiscriminative")
        in_dim = 3
        out_dim = 2    # dimension of output sequence
        max_repeat = 100000
        for SGD in [AdaGrad]:
            model = ESN(self.esn_dim, in_dim, out_dim)
            model.set_learning_rate(self.rate)
            i = tests.simple.test_real_model(model, max_repeat)
            self.assertLess(i, max_repeat)


class ESNTestCaseNumpy(NumpyTestMixin, ESNTestCase, unittest.TestCase):
    pass


class ESNTestCaseCupy(CupyTestMixin, ESNTestCase, unittest.TestCase):
    pass


if __name__ == "__main__":

    unittest.main()
