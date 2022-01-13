from ._mapping import *


def pinyin_to_zhuyin(pinyin):
    """
    Convert pinyin to zhuyin.
    """
    tone = "1"
    pinyin = pinyin.replace("v", "ü")
    for c in pinyin:
        if c.isdigit():
            tone = c
            pinyin = pinyin.replace(c, "")
            break

    return _convert(pinyin, tone, to_zhuyin=True)


def zhuyin_to_pinyin(zhuyin, u_to_v=False):
    """
    Convert zhuyin to pinyin.
    """
    tone = ""
    for c in zhuyin:
        if c in bpmf_tone:
            tone = c
            zhuyin = zhuyin.replace(c, "")
            break

    return _convert(zhuyin, tone, to_zhuyin=False, u_to_v=u_to_v)


def _convert(word, tone, to_zhuyin=True, u_to_v=False):
    """
    Convert pinyin to zhuyin or vice versa.
    """
    ret = ""
    if to_zhuyin:
        if word in p2z:
            ret = p2z[word]
        else:
            raise ValueError(f"No mapping for given pinyin input: {word}")
    else:
        if word in z2p:
            if u_to_v:
                ret = z2p[word].replace("ü", "v")
            else:
                ret = z2p[word]
        else:
            raise ValueError(f"No mapping for given zhuyin input: {word}")

    if to_zhuyin:
        ret = ret + bpmf_tone_inv[tone] if tone != "5" else bpmf_tone_inv[tone] + ret
    else:
        ret = ret + bpmf_tone[tone]

    return ret
