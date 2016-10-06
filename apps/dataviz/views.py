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
from .models import Region, Country


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/home.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        return context


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
            try:
                content_type = self.file.content_type
                name = self._save_file(self.file)

                self.request.session['error'] = False
                self.request.session['name'] = self.file.name

                if content_type == "application/vnd.ms-excel":
                    self._handle_xls_file(name)
                elif content_type == "application/octet-stream":
                    self._handle_json_file(name)
                elif content_type == "text/csv":
                    self._handle_csv_file(name)

            except Exception as e:
                self.request.session['error'] = True
            finally:
                os.remove(name)

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
                d = {}
                d['region'] = row[0]
                d['country'] = row[1]
                if row[2].isdigit():
                    d['value'] = row[2]
                else:
                    continue

                self._add_data(d)

    def _handle_json_file(self, f):
        with open(f) as data_file:
            data = json.load(data_file)
            for item in data['data']:
                d = {}
                d['region'] = item['Регион']
                d['country'] = item['Страна']
                d['value'] = item['Значение']
                self._add_data(d)

    def _handle_xls_file(self, f):
        book = xlrd.open_workbook(f)
        sh = book.sheet_by_index(0)
        for rx in range(sh.nrows):
            r = sh.row(rx)
            d = {}
            d['region'] = r[0].value
            d['country'] = r[1].value
            if str(r[2].value).isdigit():
                d['value'] = r[2].value
            else:
                continue

            self._add_data(d)

    def _add_data(self, data):
        region, r_create = Region.objects.get_or_create(name=data['region'])
        region.save()

        country, c_create = Country.objects.get_or_create(region=region, name=data['country'])
        country.value = data['value']
        country.save()


class UploadResultView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/upload_result.html'
    login_url = reverse_lazy('login')
