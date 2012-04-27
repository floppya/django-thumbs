#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import os
import django_thumbs


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
      author = django_thumbs.__author__,
      author_email = 'antonio.mele@gmail.com',
      name = django_thumbs.__title__,
      version = django_thumbs.__version__,
      description = 'Django-Thumbs is the easiest way to create thumbnails for your images with Django. Works with any StorageBackend.',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      keywords = 'django thumbs image',
      url = 'https://github.com/skitoo/django-thumbs',
      license = 'New BSD License',
      platforms = ['OS Independent'],
      classifiers = CLASSIFIERS,
      packages = find_packages()
)
