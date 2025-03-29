from django.shortcuts import render

def veri_al(request):
    isim = None
    yas = None

    if request.method == 'POST':
        # POST verilerini al
        isim = request.POST.get('isim')
        yas = request.POST.get('yas')
        
        # Veri ile işlem yapabilirsiniz (örneğin, veritabanına kaydetme vb.)
    
    return render(request, 'toplama2.html', {'isim': isim, 'yas': yas})