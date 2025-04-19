from django.shortcuts import render

from beys_world.models import AssistBlade, Bit, Blade, LockChip, MainBlade, Ratchet

def index(request):
    blades = Blade.objects.all()
    ratchets = Ratchet.objects.all()
    bits = Bit.objects.all()
    lock_chips = LockChip.objects.all()
    main_blades = MainBlade.objects.all()
    assist_blades = AssistBlade.objects.all()
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
