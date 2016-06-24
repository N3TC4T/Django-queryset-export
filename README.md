# Django Queryset Export

>  Django app to export queryset as xml and csv 

***

django queryset export allows you to export records of a queryset as csv , xml files 

###Installation
------------

* Install ``tablib`` as required module

* Install or add ``qs_export`` to your Python path.

* Add ``qs_export`` to your ``INSTALLED_APPS`` setting.

* Add ``options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('export_columns', 'exportable',)`` to your  setting.

###Usage

add ``export_columns`` and ``exportable`` tags to your model to give it export permission and exportable columns

```
class Meta:
        app_label = 'test'
        export_columns = ('col1', 'col2', 'col3', 'col4')
        exportable = True
```

then load export tag to your template

```
{% load export_tags %}
```

and in the end :

```
{% exporter "btn_text" "app_name" "model_name" %}
```

##Other

for exporting records by filter just need to pass your filters in url as GET params 
