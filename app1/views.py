from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.
def fanlar(request):
    forma = FanForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
        # yonalish_id = request.POST.get("yonalish")
        # if yonalish_id.isdigit():
        #     Fan.objects.create(
        #         nom = request.POST.get("nom"),
        #         yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
        #         asosiy = request.POST.get("asosiymi") == 'on'
        #     )
        return redirect('/fan/')
    f = Fan.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        f = Fan.objects.filter(nom__contains=soz)
    data = {
        "fan": f,
        "yonalish": Yonalish.objects.all(),
        "forma": FanForm
    }
    return render(request, "Fanlar.html", data)

def yonalish(request):
    forma = YonalishForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
        # Yonalish.objects.create(
        #     nom = request.POST.get("nom"),
        #     aktiv = request.POST.get("aktivmi") == 'on'
        # )
        return redirect('/yonalish/')
    data = {
        "yonalish": Yonalish.objects.all(),
        "forma": YonalishForm
    }
    return render(request, "Yonalish.html", data)

def ustoz(request):
    forma = UstozForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
        # Ustoz.objects.create(
        #     ism = request.POST.get('ism'),
        #     jins = request.POST.get('jins'),
        #     yosh = request.POST.get('yosh'),
        #     daraja = request.POST.get('daraja'),
        #     fan = Fan.objects.get(id=request.POST.get('fan'))
        # )
        return redirect('/ustoz/')
    u = Ustoz.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        u = Ustoz.objects.filter(ism__contains=soz)
    data = {
        "ustoz": u,
        "fan": Fan.objects.all(),
        "forma": UstozForm
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

def fan_update(request, id):
    if request.method == 'POST':
        x = Fan.objects.get(id=id)
        x.nom = request.POST.get("nom")
        x.yonalish = Yonalish.objects.get(id=request.POST.get("yonalish"))
        x.save()
        return redirect('/fan/')
    data = {
        "fan": Fan.objects.get(id=id),
        "yonalish": Yonalish.objects.all()
    }
    return render(request, "fan_update.html", data)

def yonalish_update(request, id):
    if request.method == 'POST':
        x = Yonalish.objects.get(id=id)
        x.nom = request.POST.get("nom")
        x.aktiv = request.POST.get("aktivmi")=='on'
        x.save()
        return redirect('/yonalish/')
    data = {
        'yonalish': Yonalish.objects.get(id=id)
    }
    return render(request,'yonalish_update.html', data)

def ustoz_update(request, id):
    if request.method == 'POST':
        x = Ustoz.objects.get(id=id)
        x.ism = request.POST.get('ism')
        x.jins = request.POST.get('jins')
        x.yosh = request.POST.get('yosh')
        x.daraja = request.POST.get('daraja')
        x.fan = Fan.objects.get(id=request.POST.get('fan'))
        x.save()
        return redirect('/ustoz/')
    data = {
        'ustoz': Ustoz.objects.get(id=id),
        'fan': Fan.objects.all()
    }
    return render(request, 'ustoz_update.html', data)