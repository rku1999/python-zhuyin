import unittest

from pyzhuyin import zhuyin_to_pinyin
from .dictionary import z2p, z2p_u2v


class TestZy2Py(unittest.TestCase):
    def test_zhuyin_to_pinyin(self):
        for z, p in z2p.items():
            self.assertEqual(p, zhuyin_to_pinyin(z))

        self.assertEqual(
            list(map(zhuyin_to_pinyin, list(z2p.keys()))), list(z2p.values())
        )

    def test_zhuyin_to_pinyin_u2v(self):
        for z, p in z2p_u2v.items():
            self.assertEqual(p.replace("ü", "v"), zhuyin_to_pinyin(z, u_to_v=True))

        self.assertEqual(
            list(map(lambda z: zhuyin_to_pinyin(z, u_to_v=True), list(z2p_u2v.keys()))),
            [p.replace("ü", "v") for p in z2p_u2v.values()],
        )


if __name__ == "__main__":
    unittest.main()
