#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jose

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


def get_install_requires():
    crypto_lib = 'pycryptodome >=3.3.1, <3.9.4'
    return [
        crypto_lib,
        'six <2.0',
        'ecdsa <1.0',
        'future <1.0',
    ]


setup(
    name='python-jose-cryptodome',
    version=jose.__version__,
    author='Michael Davis',
    author_email='mike.philip.davis@gmail.com',
    description='JOSE implementation in Python using pycryptodome',
    license='MIT',
    keywords='jose jws jwe jwt json web token security signing',
    url='http://github.com/capless/python-jose-cryptodome',
    packages=get_packages('jose'),
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    install_requires=get_install_requires()
)
