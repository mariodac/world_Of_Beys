from django.shortcuts import render

from beys_world.models import AssistBlade, Bit, Blade, LockChip, MainBlade, Ratchet

def index(request):
    blades = Blade.objects.all().filter(show=True)
    ratchets = Ratchet.objects.all().filter(show=True)
    bits = Bit.objects.all().filter(show=True)
    lock_chips = LockChip.objects.all().filter(show=True)
    main_blades = MainBlade.objects.all().filter(show=True)
    assist_blades = AssistBlade.objects.all().filter(show=True)
    context = {
        'blades': blades,
        'ratchets': ratchets,
        'bits': bits,
        'lock_chips': lock_chips,
        'main_blades': main_blades,
        'assist_blades': assist_blades,
        'title': 'index',
    }
    return render(
        request,
        'beys_world/index.html',
        context,
    )
