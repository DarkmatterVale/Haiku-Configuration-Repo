# This is the setup file for pip
from setuptools import setup, find_packages
import os
import sys
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    description_file = f.read()

setup(
    name = 'Haiku_Configuration_Repo',

    version = '0.0.1',

    description = 'Hardware database for Haiku',
    long_description = description_file,

    url = 'https://github.com/DarkmatterVale/Haiku-Configuration-Repo',

    author = 'Vale Tolpegin',
    author_email = 'valetolpegin@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",

        "Operating System :: OS Independent",
    ],

    packages = find_packages(),

    platforms=["any"],
      
    dependency_links = [
        'https://github.com/staticdev/django-sorting/tarball/master#egg=django-sort',
    ],
    install_requires=[
        'dj-database-url==0.4.0',
        'Django==1.9.2',
        'gunicorn==19.4.5',
        'psycopg2==2.6.1',
        'whitenoise==2.0.6'
    ],

    keywords = [ 'Haiku' ],
)
