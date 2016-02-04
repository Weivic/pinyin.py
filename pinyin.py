#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:WeiVic
"""
import os.path

__version__ = '0.9'
__all__ = ["PinYin"]


class PinYin(object):
    word_dict = {}
    word = None
    __vowels__ = 'aeiouv'
    __pinyin_dict__ = {
        'a': 'āáǎàa',
        'o': 'ōóǒòo',
        'e': 'ēéěèe',
        'i': 'īíǐìi',
        'u': 'ūúǔùu',
        'v': 'ǖǘǚǜü'
    }

    def __init__(self, word):
        self.word = word

    def __new__(cls, word):
        cls.word = word
        return object.__new__(PinYin)

    # @property
    # def vowels(self):
    #     return "aeiouv"

    @classmethod
    def load_word(cls, dict_file=None):
        if dict_file is None:
            dict_file = os.path.join(os.path.dirname(__file__), 'word.data')
        if not os.path.exists(dict_file):
            raise IOError("Data file not found!")

        with open(dict_file) as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.lower().split()
                key = line[0]
                value_raw = line[1:]
                value_pinyin = []
                value_without_number = []
                for py_raw in value_raw:
                    py_pinyin = py_raw
                    for vowel in cls.__vowels__:
                        if vowel in py_raw:
                            py_pinyin = py_raw.replace(vowel, cls.__pinyin_dict__[vowel][int(py_raw[-1])-1])[:-1]
                            break
                    value_pinyin.append(py_pinyin)
                    value_without_number.append(py_raw[:-1])
                cls.word_dict[key] = [value_raw, value_pinyin, value_without_number]

    @classmethod
    def convert(cls, convert_string=None, tone=True, num=False):
        if convert_string is None:
            if cls.word is None:
                raise TypeError("Expect convert string!")
            else:
                convert_string = cls.word
        result = []
        for char in convert_string:
            key = '%X' % ord(char)
            result.append(cls.word_dict.get(key.lower(), char)[tone and 1 or (not num and 2 or 0)])
        return result

    @classmethod
    def convert_join(cls, convert_string=None, joiner="", tone=True, num=False):
        result = cls.convert(convert_string, tone, num)
        single_list = []
        for item in result:
            single_list.append(item[0])
        return joiner.join(single_list)

if __name__ == "__main__":
    # PinYin.load_word()
    # string = "钓鱼岛是中国的"
    # print("in: %s" % string)
    # print("out: %s" % PinYin.convert_join(string, " ", False, False))
    py = PinYin("钓鱼岛是中国的")
    py.load_word()
    print(py.convert_join(joiner=" "))

