from .pinyin import PinYin
"""
A chinese pinyin converter based on @cleverdeng's pinyin.py
http://github.com/cleverdeng/pinyin.py
"""
__version__ = 0.1

_instance = PinYin()
vowels = _instance.vowels
py_dict = _instance.py_dict
load_word = _instance.load_word
convert = _instance.convert
convert_join = _instance.convert_join
pinyin = PinYin
