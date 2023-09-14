import unittest
from main_third import get_cid, get_data, get_bvid

bvid = ["BV1Ym4y1K7rg", "BV1Ap4y1E718", "BV1Ym4y1K7rg", "BV1M8411X7DP", "BV1vN411i73M", "BV1NG411d7H5"]
cid = ["1264099708", "1245630731", "1264099708", "1245291456", "1245068396", "1250757149"]


class Mytest(unittest.TestCase):

    def test_get_bvid(self):
        for i in range(6):
            bvid_data = get_bvid(i, 0)
            self.assertIsNotNone(bvid_data)

    def test_get_cid(self):
        cid_num = []
        for i in bvid:
            cid_num.append(str(get_cid(i)))
        self.assertEqual(cid, cid_num)

    def test_get_data(self):
        for i in cid:
            data = get_data(i)
            self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()