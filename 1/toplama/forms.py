from django import forms

class ToplamaFormu(forms.Form):
    sayi1 = forms.IntegerField(label='Sayı 1', required=True)
    sayi2 = forms.IntegerField(label='Sayı 2', required=True)
    