from django.shortcuts import render
from .forms import ToplamaFormu

def toplama(request):
    sonuc = None
    if request.method == "POST":
        form = ToplamaFormu(request.POST)
        if form.is_valid():
            sayi1 = form.cleaned_data['sayi1']
            sayi2 = form.cleaned_data['sayi2']
            sonuc = sayi1 + sayi2
    else:
        form = ToplamaFormu()

    return render(request, 'toplama/toplama.html', {'form': form, 'sonuc': sonuc})