from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        faces = [0, 12, 45.21, 34, 99.91]
        res = solution(faces)

        self.assertNotEqual(None, res)
        self.assertAlmostEqual(res[0], -17.777777777777779, places=3)
        self.assertAlmostEqual(res[1], -11.111111111111111, places=3)
        self.assertAlmostEqual(res[2], 7.3388888888888886, places=3)
        self.assertAlmostEqual(res[3], 1.1111111111111107, places=3)
        self.assertAlmostEqual(res[4], 37.727777777777774, places=3)
