from django import forms
from .models import Driver

class WorkForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'work_clock',
            'drive_clock',
        ]
        exclude = ('driver', 'status')

class RawWorkForm(forms.Form):
    work = forms.IntegerField()
    drive = forms.IntegerField()
    off = forms.IntegerField()
