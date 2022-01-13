from ._mapping import *


def pinyin_to_zhuyin(pinyin):
    """
    Convert pinyin to zhuyin.
    """
    pinyin = pinyin.split(" ")
    words = []
    tone = []
    for p in pinyin:
        p = p.replace("v", "ü")
        for c in p:
            if c.isdigit():
                tone.append(c)
                p = p.replace(c, "")
                break
        else:
            tone.append("1")
        words.append(p)

    return _convert(words, tone, to_zhuyin=True)


def zhuyin_to_pinyin(zhuyin, u_to_v=False):
    """
    Convert zhuyin to pinyin.
    """
    zhuyin = zhuyin.split(" ")
    words = []
    tone = []
    for z in zhuyin:
        for c in z:
            if c in bpmf_tone:
                tone.append(c)
                z = z.replace(c, "")
                break
        else:
            tone.append("")
        words.append(z)

    return _convert(words, tone, to_zhuyin=False, u_to_v=u_to_v)


def _convert(words, tone, to_zhuyin=True, u_to_v=False):
    """
    Convert pinyin to zhuyin or vice versa.
    """
    ret = []
    for w in words:
        if to_zhuyin:
            if w in p2z:
                ret.append(p2z[w])
            else:
                raise ValueError(f"No mapping for given pinyin input: {w}")
        else:
            if w in z2p:
                if u_to_v:
                    ret.append(z2p[w].replace("ü", "v"))
                else:
                    ret.append(z2p[w])
            else:
                raise ValueError(f"No mapping for given zhuyin input: {w}")

    if to_zhuyin:
        ret = [
            word + bpmf_tone_inv[tone[i]]
            if tone[i] != "5"
            else bpmf_tone_inv[tone[i]] + word
            for i, word in enumerate(ret)
        ]
    else:
        ret = [word + bpmf_tone[tone[i]] for i, word in enumerate(ret)]

    return ret
