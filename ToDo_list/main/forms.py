from django.forms import ModelForm
from django import forms
from .models import Goal


class AddGoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['details']