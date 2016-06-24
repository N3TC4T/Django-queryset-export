Django Queryset Export
=============
**Django app to export queryset as xml and csv files**

django queryset export allows you to export records of a queryset as csv , xml files 

.. contents:: Contents
    :depth: 5


Installation
------------

#. Install ``tablib`` as required module

#. Install or add ``qs_export`` to your Python path.

#. Add ``qs_export`` to your ``INSTALLED_APPS`` setting.

#. Add ``options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('export_columns', 'exportable',)`` to your  setting.


Usage
-----
