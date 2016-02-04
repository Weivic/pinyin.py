#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:WeiVic
"""
import os.path

__version__ = '0.1'
__all__ = ["PinYin"]


def load_word_dict(func):
    def wrapper(self, *args, **kwargs):
        if not any(self.word_dict):
            self.load_word()
        return func(self, *args, **kwargs)
    return wrapper


class PinYin(object):
    def __init__(self, word=None, data_file=None):
        self.word = word
        self.word_dict = {}
        if data_file is not None:
            self.load_word(data_file)

    @property
    def vowels(self):
        return 'aeiouv'

    @property
    def py_dict(self):
        return {
            'a': 'āáǎàa',
            'o': 'ōóǒòo',
            'e': 'ēéěèe',
            'i': 'īíǐìi',
            'u': 'ūúǔùu',
            'v': 'ǖǘǚǜü'
        }

    def load_word(self, data_file=None):
        if data_file is None:
            data_file = os.path.join(os.path.dirname(__file__), 'word.data')
        if not os.path.exists(data_file):
            raise IOError("Data file not found!")
        with open(data_file) as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.lower().split()
                key = line[0]
                value_raw = line[1:]
                value_pinyin = []
                value_without_number = []
                for py_raw in value_raw:
                    py_pinyin = py_raw
                    for vowel in self.vowels:
                        if vowel in py_raw:
                            py_pinyin = py_raw.replace(vowel, self.py_dict[vowel][int(py_raw[-1])-1])[:-1]
                            break
                    value_pinyin.append(py_pinyin)
                    value_without_number.append(py_raw[:-1])
                self.word_dict[key] = [value_raw, value_pinyin, value_without_number]

    @load_word_dict
    def convert(self, convert_string=None, tone=True, num=False):
        if convert_string is None:
            if self.word is None:
                raise TypeError("Expect convert string!")
            else:
                convert_string = self.word
        result = []
        for char in convert_string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key.lower(), char)[tone and 1 or (not num and 2 or 0)])
        return result

    def convert_join(self, convert_string=None, joiner="", tone=True, num=False):
        result = self.convert(convert_string, tone, num)
        single_list = []
        for item in result:
            single_list.append(item[0])
        return joiner.join(single_list)

if __name__ == "__main__":
    py = PinYin("钓鱼岛是中国的")
    print(py.convert_join(joiner=" "))

