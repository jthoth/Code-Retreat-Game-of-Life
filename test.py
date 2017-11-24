import unittest
from libs import gamelife
import numpy as np

class ConwayTest(unittest.TestCase):

    def setUp(self):
        self.obj_conway = gamelife.GameOfLife()

    def test_given_3x3_matriz_and_6_neighbors_point_1_1_cell_died(self):

        mat_input = np.asarray([[255,0,255],[255,255,255],[0,0,255]])
        mat_expected = np.asarray([[255,0,255],[255,0,255],[0,0,255]])
        total = self.obj_conway.compute_total(mat_input, 1, 1, 3)
        mat_result = self.obj_conway.survive_or_die(mat_input, mat_input,1,1,total)
        resultado = np.array_equal(mat_expected,mat_result)

        self.assertEqual(resultado, True)

    def test_given_3x3_matriz_and_3_neighbors_point_1_1_cell_alive(self):

        mat_input = np.asarray([[0,0,255],[0,255,0],[0,0,255]])
        mat_expected = np.asarray([[0,0,255],[0,255,0],[0,0,255]])
        total = self.obj_conway.compute_total(mat_input, 1, 1, 3)
        mat_result = self.obj_conway.survive_or_die(mat_input, mat_input,1,1,total)
        resultado = np.array_equal(mat_expected,mat_result)

        self.assertEqual(resultado, True)


if __name__ == '__main__':
    unittest.main()
