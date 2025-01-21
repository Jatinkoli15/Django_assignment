from django.shortcuts import render
from django.http import HttpResponse




def not_found(request):
    return HttpResponse(
        '''
           <h1> Not found Page </h1>
           <a href="/">Go to home </a>
            
'''
    )