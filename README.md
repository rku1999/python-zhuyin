# Python-Zhuyin (pyzhuyin) 注音和拼音轉換

## Introduction 介紹
pyzhuyin is an open source Python library that provides a unified interface for converting between Chinese pinyin and Zhuyin (bopomofo).

pyzhuyin 是一個開放原始碼的 Python 套件，提供了將拼音轉換成注音的統一介面。

## Installation 安裝
```shell
pip install pyzhuyin
```

## Usage 使用
```python
from pyzhuyin import pinyin_to_zhuyin, zhuyin_to_pinyin


assert(pinyin_to_zhuyin("lu3 dan4") == ["ㄌㄨˇ", "ㄉㄢˋ"])
assert(zhuyin_to_pinyin("ㄌㄨˇ ㄉㄢˋ") == ["lu3", "dan4"])

assert(zhuyin_to_pinyin("ㄌㄩˊ ˙ㄗ") == ["lü2", "zi5"])
assert(zhuyin_to_pinyin("ㄌㄩˊ ˙ㄗ", u_to_v=True) == ["lv2", "zi5"])
```

## Testing 測試
Run the following command at the root of the project to test the library:

在根目錄執行以下指令以測試套件:
```shell
python3 -m unittest
```

## Notes 備註
- Only support numeric tone for pinyin
    - e.g. "lu3" instead of "lǔ" 
- Neutral tone is represented as 5
    - e.g. "˙ㄗ" -> "zi5"
- For pinyin_to_zhuyin:
    - if corresponding zhuyin not found, raise ValueError
    - internally convert all v to ü
- For zhuyin_to_pinyin:
    - if corresponding pinyin not found, raise ValueError
- [兒化音](https://zh.wikipedia.org/wiki/%E5%85%92%E5%8C%96) is not supported because it is not representable in the zhuyin system as a "combo" word
    - e.g. "公園兒" -> "gong1 yuanr2" -> "ㄍㄨㄥ ㄩㄢㄦˊ" (not allowed)

## Data Sources 資料來源
- 中華民國教育部（Ministry of Education, R.O.C.）。《重編國語辭典修訂本》（版本編號：2015_20210928 ）

    網址：https://dict.revised.moe.edu.tw/ 
    
    [CC BY-ND 3.0 TW 授權](https://creativecommons.org/licenses/by-nd/3.0/tw/legalcode)

## Author 作者
- Raymond Ku