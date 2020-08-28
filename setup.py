#!/usr/bin/env python

from os.path import exists
from setuptools import setup

packages = ['sensorflow', 'sensorflow.dataframe']

tests = [p + '.tests' for p in packages]


setup(name='sensorflow',
      version='0.0.1',
      description='Sensorflow API',
      maintainer='gkamath',
      packages=packages + tests,
      python_requires='>=3.6',
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      zip_safe=False)
