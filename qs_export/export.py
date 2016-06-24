from django.db.models import Q
from django.http import HttpResponse
import csv
import tablib


class Exporter(object):
    def __init__(self, model, filters, request):
        self._model = model
        self._filters = filters
        self._request = request
        self._queryset = self.mixin_data()

    def mixin_data(self):
        qset = Q()
        for field, value in self._filters.items():
            qset &= Q(**{field: value})
        if qset:
            queryset = self._model.objects.filter(qset).only(
                *self._model._meta.export_columns)
        else:
            queryset = self._model.objects.only(
                *self._model._meta.export_columns)

        return queryset

    # exporters modules

    def xls_exporter(self):
        headers = self._model._meta.export_columns
        data = []
        data = tablib.Dataset(*data, headers=headers)
        for obj in self._queryset:
            row = []
            for field in self._model._meta.export_columns:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                if type(val) == unicode:
                    val = val.encode("utf-8")
                row.append(val)
            data.append(row)
        response = HttpResponse(data.xls, content_type='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=export.xls"
        return response

    def csv_exporter(self):
        response = HttpResponse(content_type='application/x-download')
        response['Cache-Control'] = 'no-cache'
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        writer.writerow(self._model._meta.export_columns)
        # CSV Data
        for obj in self._queryset:
            row = []
            for field in self._model._meta.export_columns:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                if type(val) == unicode:
                    val = val.encode("utf-8")
                row.append(val)
            writer.writerow(row)

        return response

    # TODO: add pdf support
    def pdf_exporter(self):
        return 'pdf export file requested'
