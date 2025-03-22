from django.shortcuts import render
from django.http import JsonResponse

counter = 0  # Sayacı burada tutuyoruz (not: bu sadece geçici; sayfa yenilenince sıfırlanır)

def anasayfa(request):
    return render(request, 'home/anasayfa.html', {'counter': counter})

def sayaci_artir(request):
    global counter
    counter += 1
    #return render(request, 'home/anasayfa.html', {'counter': counter})

    return JsonResponse({'counter': counter})