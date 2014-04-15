#! /usr/bin/env python
from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.7'
PROJECT_NAME = 'ZQTable'
PROJECT_AUTHORS = "Salim Fadhley"
# Please see readme.rst for a complete list of contributors
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://bitbucket.org/salimfadhley/zqtable"
SHORT_DESCRIPTION = 'Tabular and time-sequence data in pure python'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.rst")).read()
except IOError as _:
    DESCRIPTION = SHORT_DESCRIPTION


setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    py_modules=['zqtable'],
    zip_safe=True,
    include_package_data=False,
    #install_requires=['blist'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage'],
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    use_2to3=True,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
)
