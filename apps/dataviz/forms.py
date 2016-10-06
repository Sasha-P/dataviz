from django import forms
from django.core.exceptions import ValidationError


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_file(self):
        file = self.cleaned_data.get("file", False)
        poz = file.name.index('.')
        if poz > -1:
            poz += 1
        else:
            raise ValidationError("File format is invalid.")
        filetype = file.name[poz:].lower()
        if not filetype in ['csv', 'json', 'xls']:
            raise ValidationError("File format is invalid.")
        return file
