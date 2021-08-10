# Copyright (c) 2021 - Itz-fork
# Project: py_extract
import os
from setuptools import setup, find_packages

# Allow Exec. from any path (Credits: mega.py)
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Getting the requirements
if os.path.isfile('requirements.txt'):
  with open('requirements.txt') as req:
    reques = req.read().splitlines()
else:
  reques = [
    'ffmpeg'
  ]

# Getting the long description
if os.path.isfile('README.md'):
  with open(('README.md'), encoding='utf-8') as readmeh:
    big_description = readmeh.read()
else:
  big_description = "Py_extract is a simple, light-weight python library to handle some extraction tasks using less lines of code."


setup(name='py_extract',
version='0.0.1',
description='Py_extract is a simple, light-weight python library to handle some extraction tasks using less lines of code.',
url='https://github.com/Itz-fork/py-extract',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
download_url="https://github.com/Itz-fork/py-extract",
keywords=['python', 'extract', 'py-extract'],
long_description=big_description,
long_description_content_type='text/markdown',
install_requires=reques,
classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Multimedia',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)