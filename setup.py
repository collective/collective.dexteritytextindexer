# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '2.4.1.dev0'

tests_require = [
    'zope.configuration',
    'plone.testing',
    'plone.app.testing',
    'plone.autoform',
]

setup(
    name='collective.dexteritytextindexer',
    version=version,
    description="Dynamic SearchableText index for dexterity content types",
    long_description=(
        open("README.rst").read() +
        '\n' +
        open("CHANGES.rst").read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone :: 5.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone dexterity searchable text indexer',
    author='Jonas Baumann',
    author_email='mailto:info@4teamwork.ch',
    url='http://github.com/collective/collective.dexteritytextindexer',
    license='GPL2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'six',
        'plone.api',
        'plone.app.dexterity',
        'plone.behavior',
        'plone.dexterity',
        'plone.indexer',
        'plone.supermodel >= 1.1.1',
        'plone.z3cform',
        'Products.CMFCore',
        'setuptools',
        'z3c.form',
        'ZODB3',
        'zope.component',
        'zope.deferredimport',
        'zope.interface',
        'zope.schema',
    ],
    tests_require=tests_require,
    extras_require=dict(
        tests=tests_require,
        namedfile=['plone.namedfile']
    ),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
