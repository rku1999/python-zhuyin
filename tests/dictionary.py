p2z = {
    "ni3 hao3": ["ㄋㄧˇ", "ㄏㄠˇ"],
    "zhong1 wen2": ["ㄓㄨㄥ", "ㄨㄣˊ"],
    "zhong4 xin1": ["ㄓㄨㄥˋ", "ㄒㄧㄣ"],
    "jiao4 yu4 bu4": ["ㄐㄧㄠˋ", "ㄩˋ", "ㄅㄨˋ"],
    "ȇ4": ["ㄝˋ"]
}

p2z_u2v = {
    "lü4 zui3": ["ㄌㄩˋ", "ㄗㄨㄟˇ"],
    "lv4 guo1": ["ㄌㄩˋ", "ㄍㄨㄛ"],
    "lve4 gao1 yi1 chou2": ["ㄌㄩㄝˋ", "ㄍㄠ", "ㄧ", "ㄔㄡˊ"],
    "lüe4 dong3": ["ㄌㄩㄝˋ", "ㄉㄨㄥˇ"],
    "lu3 dan4": ["ㄌㄨˇ", "ㄉㄢˋ"],
}

z2p = {" ".join(v): k.split(" ") for k, v in p2z.items()}

z2p_u2v = {" ".join(v): k.split(" ") for k, v in p2z_u2v.items()}