from django import forms

class ContohForm(forms.Form):
    nama = forms.CharField(max_length=100)
    email = forms.EmailField()
    pesan = forms.CharField(widget=forms.Textarea)
