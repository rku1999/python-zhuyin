import unittest

from pyzhuyin import zhuyin_to_pinyin
from .dictionary import z2p


class TestZy2Py(unittest.TestCase):
    def test_zhuyin_to_pinyin(self):
        for z, p in z2p.items():
            self.assertEqual(p, zhuyin_to_pinyin(z))

    def test_zhuyin_to_pinyin_u2v(self):
        for z, p in z2p.items():
            self.assertEqual(p, zhuyin_to_pinyin(z, u_to_v=True))


if __name__ == "__main__":
    unittest.main()
