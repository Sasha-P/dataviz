from django.views.generic import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

import os
import csv
import xlrd
import json
from datetime import datetime

from .forms import UploadFileForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/home.html'
    login_url = reverse_lazy('login')


class UploadFileFormView(LoginRequiredMixin, FormView):
    template_name = 'dataviz/upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('dataviz:upload_result')
    login_url = reverse_lazy('login')
    file = None

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.file = request.FILES['file']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if self.file:
            content_type = self.file.content_type
            name = self._save_file(self.file)
            if content_type == "application/vnd.ms-excel":
                self._handle_xls_file(name)
            elif content_type == "application/octet-stream":
                self._handle_json_file(name)
            elif content_type == "text/csv":
                self._handle_csv_file(name)

            self.request.session['name'] = self.file.name

        self.file = None
        return super().form_valid(form)

    def _save_file(self, f):
        name = str(datetime.now()).replace(':', '_') + '___' + f.name
        with open(name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return name

    def _handle_csv_file(self, f):
        with open(f, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csv_reader:
                print(', '.join(row))
        os.remove(f)

    def _handle_json_file(self, f):
        with open(f) as data_file:
            data = json.load(data_file)
            print(data)
        os.remove(f)

    def _handle_xls_file(self, f):
        book = xlrd.open_workbook(f)
        sh = book.sheet_by_index(0)
        for rx in range(sh.nrows):
            print(sh.row(rx))
        os.remove(f)


class UploadResultView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/upload_result.html'
    login_url = reverse_lazy('login')
