"""click_tracker URL Configuration
"""
import random

from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect

def give_response(request):
    # if random.random() > 0.5:
    #     return HttpResponseRedirect('/1')
    html = "<html><body>Silence in Beautiful.</body></html>"
    return HttpResponse(html)

def give_response_1(request):
    if random.random() > 0.5:
        return HttpResponseRedirect('/2')
    html = "<html><body>Silence in Beautiful 1.</body></html>"
    return HttpResponse(html)

def give_response_2(request):
    if random.random() > 0.5:
        return HttpResponseRedirect('/3')
    html = "<html><body>Silence in Beautiful 2.</body></html>"
    return HttpResponse(html)

def give_response_3(request):
    html = "<html><body>Silence in Beautiful 3.</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', give_response),
    path('1/', give_response_1),
    path('2/', give_response_2),
    path('3/', give_response_3),
]

