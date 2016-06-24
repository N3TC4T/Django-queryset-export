# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import get_model
from django.core import signing
from export import Exporter
import json


@login_required
def ExporterView(request):
    # check if request is post if not raise Forbidden error
    if not request.method == 'POST':
        return HttpResponseForbidden()

    # try:
    # set legal types to export
    types = ['csv', 'xls', 'pdf']

    # pass all POST params
    export_type = request.POST['type']
    export_model = signing.loads(request.POST['model'])
    export_app = signing.loads(request.POST['app'])
    export_filters = request.POST['filters']

    # check if export type is on legal list
    if export_type not in types:
        return HttpResponseNotAllowed()

    # get model object
    model = get_model(export_app, export_model)
    filters = json.loads(export_filters)

    # check if model is exportable
    if not model._meta.exportable:
        return HttpResponseNotAllowed()

    exporter = Exporter(model, filters, request)

    if export_type == 'xls':
        response = exporter.xls_exporter()
    elif export_type == 'pdf':
        response = exporter.pdf_exporter()
    elif export_type == 'csv':
        response = exporter.csv_exporter()

    return response

    # except Exception as error:
    #     return HttpResponse(error)
