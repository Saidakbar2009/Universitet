from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def fanlar(request):
    f = Fan.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        f = Fan.objects.filter(nom__contains=soz)
    data = {
        "fan": f
    }
    return render(request, "Fanlar.html", data)

def yonalish(request):
    data = {
        "yonalish": Yonalish.objects.all()
    }
    return render(request, "Yonalish.html", data)

def ustoz(request):
    u = Ustoz.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        u = Ustoz.objects.filter(ism__contains=soz)
    data = {
        "ustoz": u
    }
    return render(request, "Ustoz.html", data)

def fan_ochir(request, son):
    Fan.objects.filter(id=son).delete()
    return redirect("/fan/")

def yonalish_ochir(request, son):
    Yonalish.objects.filter(id=son).delete()
    return redirect('/yonalish/')