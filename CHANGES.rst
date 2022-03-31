Changelog
=========


2.4.1 (2022-03-31)
------------------

- Fixed duplicated values in SearchableText.
  [gbastien]

- Fix a bug in the RichText field indexer on Python 3.
  [alecpm]


2.4.0 (2020-01-24)
------------------

- Add behavior shortname "collective.dexteritytextindexer"
  [agitator]


2.3.0 (2019-09-27)
------------------

- A few updates to make build pass on travis again, i.e.
  add index/allow-hosts to buildout configs,
  set version.cfg reference to 'latest' for 5.0.x,
  bump setuptools and zc.buildout versions
  [staeff]

- Update the Add-On to also run in Plone 5.2 with Python 3.
  Fixes https://github.com/collective/collective.dexteritytextindexer/issues/31
  [staeff]


2.2.1 (2017-07-26)
------------------

- Fix a bug in the RichText field indexer when the value of RichText field is None.
  The bug was introduced in 2.2.0.
  [mbaechtold]


2.2.0 (2017-06-23)
------------------

- Added TupleFieldConverter, to enable indexing of portal catalog KeywordIndex indices.
  [jone, mtrebron, maurits]

- Improved code quality.  [maurits]

- Add the ability to index a RichText field. Fixes #23.
  [smcmahon]


2.1.1 (2016-11-03)
------------------

- Remove traces of plone.directives.form (which implicitly added grok as a dependency).
  [gforcada]

- Silent a plone.behavior warning.
  [gforcada]

- Specify compatibility in setup.py for versions which are tested and remove
  unittest2 dependency
  [tomgross]

2.1.0 (2016-04-14)
------------------

- Add schemaeditor support
  [datakurre]


2.0.2 (2016-04-07)
------------------

- Handle indexing from scripts.
  Fixes https://github.com/collective/collective.dexteritytextindexer/issues/12
  [gforcada]


2.0.1 (2014-01-02)
------------------

- Fix encoding error when transforming HTML to text.
  [jone]


2.0 (2013-03-16)
----------------

- Drop Plone 4.1 support.
  [jone]

- Mark title and description of p.a.dexterity's IBasic
  as searchable by default.
  [jone]

- Add a no_longer_searchable utility function.
  [jone]

- Plone 4.3 support.
  [jone]

- Eliminate grok / martian dependencies in favor of the new plone.supermodel directives. #5
  [jone]


1.5.1 (2013-02-20)
------------------

- Do not try to convert text/plain in files, just index it as it is.
  [zupo]


1.5 (2012-08-16)
----------------

- Fix missing field bug. #3

  - Log an error when indexing an object and one of its schemas defines a missing
    field as searchable.

  - Make sure that indexing other existing fields of the same schema works.

  - searchable utils function: raise AttributeError when field is missing.

  [jone]

- Added support for marking fields searchable in plone.supermodel XML models.
  This is done by implementing a IFieldMetadataHandler that is capable of
  serializing/de-serializing the corresponding taggedValue to/from XML.
  [lgraf]

- Add ``utils.searchable`` method for marking fields of third party schemas as searchable.
  [kagesenshi]


1.4.1 (2011-11-17)
------------------

- ignore the request in the get_field_widget method, to avoid problems with request variables wich have the same name than the field.
  [phgross]

- Added test-buildout for plone-4.1.x
  [lgraf]


1.4 (2011-08-24)
----------------

- Added IntFieldConverter, wich return the plain value instead of the render method (600000 --> 600,000)
  [phgross]


1.3
---

- Fixed querying of tagged values: use helper function mergedTaggedValueList - which also looks
  up tagged values on superclasses.
  [jbaumann]

- Fixed html to text transform call: added source mimetype.
  [jbaumann]


1.2
---

- Fixed data transforms in NamedFileConverter
  [lgraf]


1.1
---

- Made reindexer more robust, since sometimes the field values may be wrong.
  [jbaumann]

- Do not traverse to "view" in indexer, this could cause security issues especially in tests.
  Using now a fake-view for enabling z2 mode.
  [jbaumann]


1.0
---

- Fixed assertion bug when using a `IDynamicTextIndexExtender` adapter.
  [jbaumann]


1.0b3
-----

- Moved `IDynamicTextIndexExtender` to `interfaces` module.
  [jbaumann]

- The `plone.namedfile` is now optional. The new namedfile converting
  adapter is only registered if its present
  [jbaumann]

- Re-implemented converting of field data with an newly introduced adapter.
  The default converter just converts the widget in display mode and
  transforms it to text/plain.
  [jbaumann]

- Fixed tests for compaitbility with plone.app.testing 4.0a3: Use TEST_USER_ID instead of TEST_USER_NAME
  [jbaumann]

- fixed Bug UnicodeError:  while indexing lists  or dicts with special chars (Non-Ascii characters)
  [phgross]


1.0b2
-----

- Fixed MANIFEST.in
  [jbaumann]


1.0b1
-----

- Initial release
