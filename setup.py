# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Poe-Profile',
    version='0.1.0',
    description='Package to retrieve data publicly available from the GGG Website.',
    long_description=readme,
    author='Fabian Widmann',
    author_email='fabian.widmann@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

