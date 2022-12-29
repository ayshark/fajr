# from django import forms
from django.forms import ModelForm
from .models import Tracker

class TrackerForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ['date', 'daily_status']
        # fields = "__all__"

        # widgets = {
        #     # 'date': forms.DateInput(format='%d\/%m\/%Y'),
        #     # 'daily_status': forms.CharField()
        # }
