#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
"""
from distutils.core import setup
from . import __version__ as version

setup(
            name='pinyin',
            version=version,
            description='A chinese pinyin converter, 中文拼音转换器',
            author='WeiVic',
            author_email='weivic@yeah.net',
            url='http://github.com/cleverdeng/pinyin.py',
            py_modules=['pinyin'],
            license='MIT License',
            platforms=['any'],
            classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries',
                'Topic :: Software Development :: Libraries :: Python Modules'
                ]
                    
    )
