#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = "0.1.0"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
setup(
    name="numbercards",
    version=version,
    description = "Create batches of simple number cards",
    long_description=read('README.md'),
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords = "numbers, cards, poster, conference tool",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/numbercards",
    download_url = r"https://github.com/lambdalisue/numbercards/tarball/master",
    license = 'MIT',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = True,
    install_requires=[
        'setuptools',
        'reportlab',
    ],
    entry_points={
        'console_scripts': [
            'numbercards = numbercards.numbercards:main',
        ],
    },
)
