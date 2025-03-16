import os
import sys
import json
from datetime import datetime
from pathlib import Path

import django
from django.conf import settings
from django.core.files import File

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    from beys_world.models import Blade

    Blade.objects.all().delete()

    django_blades = []

    with open(
        Path(__file__).parent / "all-parts-beyblades.json", "r", encoding="utf-8"
    ) as f_json:
        beyblades_parts = json.load(f_json)

    for item in beyblades_parts.get("Blades"):

        file_name = os.path.basename(item.get("Image Path"))
        if item.get("Image Path") != "N/A" and item.get("Image Path") != "":
            path =  item.get("Image Path").replace('%USERPROFILE%', '')
            file_image = open(os.path.normpath(os.environ['USERPROFILE'] + path), "rb")
            django_blades.append(
                Blade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_Hasbro=item.get("Hasbro Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    link_fandom=item.get("Link Blades"),
                )
            )
        else:
            django_blades.append(
                Blade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_Hasbro=item.get("Hasbro Name"),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    link_fandom=item.get("Link Blades"),
                )
            )
    if len(django_blades) > 0:
        Blade.objects.bulk_create(django_blades)
    
