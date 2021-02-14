from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
# Create your views here.


def search(request):
    return HttpResponse('this is search for dict')

def word_details(request, word):

    #check if word is valid
    for char in word:
        if char.isdigit():
            return HttpResponseBadRequest()

    return HttpResponse(word)