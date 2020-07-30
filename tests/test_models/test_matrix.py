import models
from models.matrix import Matrix
import unittest

class Test_Matrix(unittest.TestCase):

    def instantiateMatrixClass(self):
        instance = Matrix(4,4)        
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()