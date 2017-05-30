from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        faces = [0, 12, 45.21, 34, 99.91]
        res = solution(faces)

        self.assertNotEqual(None, res)
        self.assertEqual(res[0], -17.777777777777779)
        self.assertEqual(res[1], -11.111111111111111)
        self.assertEqual(res[2], 7.3388888888888886)
        self.assertEqual(res[3], 1.1111111111111107)
        self.assertEqual(res[4], 37.727777777777774)
