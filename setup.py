from setuptools import setup, find_packages
import os

version = '1.5.2.dev0'

tests_require = [
    'zope.testing',
    'zope.schema',
    'plone.app.testing',
    'plone.autoform',
    'plone.testing',
    ]

setup(name='collective.dexteritytextindexer',
      version=version,
      description="Dynamic SearchableText index for dexterity content types",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Jonas Baumann',
      author_email='mailto:info@4teamwork.ch',
      url='http://github.com/collective/collective.dexteritytextindexer',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.indexer',
        'plone.behavior',
        'zope.interface',
        'plone.directives.form',
        'plone.dexterity',
        'plone.supermodel',
        'plone.z3cform',
        'z3c.form',
        'elementtree',
        ],
      tests_require=tests_require,
      extras_require=dict(
        tests=tests_require,
        namedfile=['plone.namedfile']),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
