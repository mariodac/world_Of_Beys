from django.shortcuts import render

from beys_world.models import Blade

def index(request):
    blades = Blade.objects.all()
    context = {
        'blades': blades
    }
    return render(
        request,
        'beys_world/index.html',
        context,
    )
