from django.shortcuts import render
from django.utils.translation import gettext_lazy as _ 

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
        "title": _("All Parts"),
    }
    return render(
        request,
        'beys_world/all_parts.html',
        context
    )