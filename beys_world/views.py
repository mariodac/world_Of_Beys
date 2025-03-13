from django.shortcuts import render

def index(request):
    return render(
        request,
        'beys_world/index.html',
    )
