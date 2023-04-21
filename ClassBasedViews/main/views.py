from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone


class TimeTemplateView(TemplateView):
    template_name = 'templateView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()

        return context 