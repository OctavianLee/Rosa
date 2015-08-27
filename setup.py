# -*- coding: utf-8 -*-
"""
Cytisas is a suit for pytest.
"""

from setuptools import setup, find_packages

URL = "https://github.com/OctavianLee/Cytisas"
VERSION = “0.0.1”

setup(
    name=“Rosa”,
    version=VERSION,
    license='MIT',
    author="Octavian Lee",
    author_email="octavianlee1@gmail.com",
    url=URL,
    description="A suite for pytest.”,
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
)
