#!/usr/bin/env python

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup


setup(name='txTemplate',
      version='1.0.0',
      description='Twisted Adapters for Templating Engines',
      long_description=open("README.rst", "r").read(),
      author='Mike Steder',
      author_email='steder@gmail.com',
      url='http://bitbucket.org/steder/txtemplate',
      packages=['txtemplate',],
      test_suite="txtemplate.test",
      install_requires=["genshi",
                        "twisted"],
     )