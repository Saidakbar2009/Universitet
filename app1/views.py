from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def fanlar(request):
    if request.method == 'POST':
        yonalish_id = request.POST.get("yonalish")
        if yonalish_id.isdigit():
            Fan.objects.create(
                nom = request.POST.get("nom"),
                yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
                asosiy = request.POST.get("asosiymi") == 'on'
            )
        return redirect('/fan/')
    f = Fan.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        f = Fan.objects.filter(nom__contains=soz)
    data = {
        "fan": f,
        "yonalish": Yonalish.objects.all()
    }
    return render(request, "Fanlar.html", data)

def yonalish(request):
    if request.method == 'POST':
        Yonalish.objects.create(
            nom = request.POST.get("nom"),
            aktiv = request.POST.get("aktivmi") == 'on'
        )
        return redirect('/yonalish/')
    data = {
        "yonalish": Yonalish.objects.all()
    }
    return render(request, "Yonalish.html", data)

def ustoz(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism = request.POST.get('ism'),
            jins = request.POST.get('jins'),
            yosh = request.POST.get('yosh'),
            daraja = request.POST.get('daraja'),
            fan = Fan.objects.get(id=request.POST.get('fan'))
        )
        return redirect('/ustoz/')
    u = Ustoz.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        u = Ustoz.objects.filter(ism__contains=soz)
    data = {
        "ustoz": u,
        "fan": Fan.objects.all()
    }
    return render(request, "Ustoz.html", data)

def fan_ochir(request, son):
    Fan.objects.filter(id=son).delete()
    return redirect("/fan/")

def yonalish_ochir(request, son):
    Yonalish.objects.filter(id=son).delete()
    return redirect('/yonalish/')

def asosiy(request):
    return HttpResponse("Salom!")