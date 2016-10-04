from django.views.generic import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UploadFileForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/home.html'
    login_url = reverse_lazy('login')


class UploadFileFormView(LoginRequiredMixin, FormView):
    template_name = 'dataviz/upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('dataviz:upload_result')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        return super(UploadFileFormView, self).form_valid(form)


class UploadResultView(LoginRequiredMixin, TemplateView):
    template_name = 'dataviz/upload_result.html'
    login_url = reverse_lazy('login')
