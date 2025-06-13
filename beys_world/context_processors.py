from django.utils import translation
from beys_world.models import Blade, AssistBlade, Bit, LockChip, MainBlade, Ratchet


def site_context(request):
    return {
        "html_language": translation.get_language(),
        "parts": {
            "blades": Blade.objects.all(),
            "assist_blades": AssistBlade.objects.all(),
            "bits": Bit.objects.all(),
            "lockchips": LockChip.objects.all(),
            "main_blades": MainBlade.objects.all(),
            "ratchets": Ratchet.objects.all(),
        },
    }
