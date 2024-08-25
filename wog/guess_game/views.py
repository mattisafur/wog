from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

# TODO: test view function, remove
def test_render(request: HttpRequest) -> HttpResponse:
    return render(request, "hello.html")
