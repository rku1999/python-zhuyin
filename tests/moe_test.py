import json
from pyzhuyin.convert import pinyin_to_zhuyin, zhuyin_to_pinyin
from pyzhuyin._mapping import *


def read_trie(trie, words):
    if "w" in trie:
        w_lists = [el for sub in trie["w"].values() for el in sub]
        words.extend(w_lists)
    if "c" in trie:
        for c in trie["c"]:
            read_trie(trie["c"][c], words)


def get_words(fname):
    with open(fname) as f:
        data = json.load(f)
    
    words = []
    for w in data:
        read_trie(data[w], words)
    
    return words

SKIPPED = []
INCLUDED = set()

if __name__ == "__main__":
    words = get_words("trie_moedict.json")

    for w in words:
        if any('r' in c[-2:] for c in w['p']):
            print(f"Skipping: {w['ch']}")
            SKIPPED.append(w['ch'])
            continue

        print(f"Processing: {w['ch']}")
        zhuyin = pinyin_to_zhuyin(' '.join(w["p"]))
        pinyin = zhuyin_to_pinyin(' '.join(w["b"]), u_to_v=True)

        if zhuyin != w["b"]:
            print(f"Correct zhuyin: {w['b']}, got: {zhuyin}")
            break
        else:
            for z in zhuyin:
                for c in z:
                    if c in bpmf_tone:
                        z = z.replace(c, "")
                        break
                INCLUDED.add(z)
        if pinyin != w["p"]:
            print(f"Correct pinyin: {w['p']}, got: {pinyin}")
            break
        
    
    # with open("skipped.json", "w") as f:
    #     json.dump(SKIPPED, f)
    # with open("included.json", "w") as f:
    #     json.dump(list(INCLUDED), f)

    print(len(words))
    print(len(INCLUDED))
    print(len(z2p.keys()))
    print(z2p.keys() - INCLUDED)
