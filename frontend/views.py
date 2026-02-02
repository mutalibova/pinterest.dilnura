from django.shortcuts import render
from .models import *





def home(request):
    main = Movie.objects.all()
    banner = Mainn.objects.all()
    main_banner = Main_Movie.objects.all()
    return render(request, "home.html", {"main_banner": main_banner, "main": main, "banner": banner })