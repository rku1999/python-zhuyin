import unittest

from pyzhuyin.convert import pinyin_to_zhuyin
from .dictionary import p2z, p2z_u2v


class TestPy2Zy(unittest.TestCase):
    def test_pinyin_to_zhuyin(self):
        for p, z in p2z.items():
            self.assertEqual(z, pinyin_to_zhuyin(p))

    def test_pinyin_to_zhuyin_u2v(self):
        for p, z in p2z_u2v.items():
            self.assertEqual(z, pinyin_to_zhuyin(p))


if __name__ == "__main__":
    unittest.main()
