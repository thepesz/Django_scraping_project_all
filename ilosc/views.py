import requests
from ilosc.words_counter import words_counter
from django.http import HttpResponse



def scrap(request):

    words_counter()
    message = "Baza została zaktualizowana"

    return HttpResponse(message)









