from django.shortcuts import render

from beys_world.models import AssistBlade, Bit, Blade, LockChip, MainBlade, Ratchet

def index(request):
    context = {
        "title": "Home",
    }
    return render(
        request,
        'beys_world/index.html',
        context
    )

def all_parts(request):
    context = {
        "title": "All Parts",
    }
    return render(
        request,
        'beys_world/all_parts.html',
        context
    )