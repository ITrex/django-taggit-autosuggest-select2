# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

os.chdir(BASE_PATH)

long_description = open('README.txt').read()

setup(
    name='django-taggit-autosuggest-select2',
    version='0.1',
    description='Autosuggestions for django-taggit',
    long_description=long_description,
    author='Fabian Topfstedt',
    author_email='topfstedt@schneevonmorgen.com',
    url='https://bitbucket.org/fabian/django-taggit-autosuggest',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=[
        'django-taggit',
    ],
)
