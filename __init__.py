from .pinyin import PinYin

_instance = PinYin()
vowels = _instance.vowels
py_dict = _instance.py_dict
load_word = _instance.load_word
convert = _instance.convert
convert_join = _instance.convert_join
pinyin = PinYin
