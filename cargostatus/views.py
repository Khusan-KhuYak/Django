from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cargostatus

# получение данных из бд
def index(request):
    person = cargostatus.objects.all()
    return render(request, "cargostatus.html", {"cargostatus": cargostatus})

# сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         tom = Person()
#         tom.name = request.POST.get("name")
#         tom.age = request.POST.get("age")
#         tom.save()
#     return HttpResponseRedirect("/")
# Create your views here.
