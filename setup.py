#!/usr/bin/env python3

from distutils.core import setup

setup(
  name='twinrinks',
  version='1.0',
  description='Twin Rinks Hockey Calendar Scraper',
  author='Fred Fettinger',
  author_email='fettinge@gmail.com',
  url='https://github.com/BinaryMan32/twinrinks',
  packages=[],
  install_requires=['lxml'],
  scripts=['scripts/twinrinks'],
)
