"""A setuptools based setup module.

See:
https://github.com/FreeTHX/pywakepsXonbt
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open
import wakepsXonbt

NAME = 'pywakepsXonbt'
DESCRIPTION = 'A Python library to wakeup PlayStation (ps3, ps4, ps5) on BlueTooth'
URL = 'https://github.com/FreeTHX/pywakepsXonbt'
AUTHOR = 'FreeTHX'
AUTHOR_EMAIL = 'freethx.dev@gmail.com'
REQUIRED = ['pyusb']

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
try:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=NAME,
    version=wakepsXonbt.__version__,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='Apache License 2.0',
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    keywords='wake playstation (ps3, ps4, ps5) on bt home assistant',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=REQUIRED,
)
