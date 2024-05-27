# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dynamodb',
    version='0.1.2', # increase version by 0.0.1
    description='Downloads and prepares db movie data',
    long_description=readme,
    author='Safouan Er-Ryfy',
    author_email='safouan.erryfy@stud.h-da.de',
    url='https://code.fbi.h-da.de/safouan.erryfy/dynamodb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
