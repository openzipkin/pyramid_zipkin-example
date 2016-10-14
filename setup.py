#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyramid_zipkin-example',
    version='0.1',
    author='OpenZipkin',
    author_email='zipkin-user@googlegroups.com',
    license='Apache 2.0',
    url='https://github.com/openzipkin/pyramid_zipkin-example',
    description='See how much time python services spend on an http request',
    install_requires=[
        'wsgiref',
        'pyramid',
        'requests',
        'pyramid_zipkin',
    ]
)
