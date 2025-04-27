import os
import sys
import json
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
    from beys_world.models import Blade, Ratchet, Bit, LockChip, MainBlade, AssistBlade
    from utils import Utils
    utils = Utils()

    Blade.objects.all().delete()
    Ratchet.objects.all().delete()
    Bit.objects.all().delete()
    LockChip.objects.all().delete()
    MainBlade.objects.all().delete()
    AssistBlade.objects.all().delete()

    django_blades = []
    django_ratchets = []
    django_bits = []
    django_lock_chips = []
    django_main_blades = []
    django_assist_blades = []

    with open(
        Path(__file__).parent / "all-parts-beyblades.json", "r", encoding="utf-8"
    ) as f_json:
        beyblades_parts = json.load(f_json)

    for item in beyblades_parts.get("Blades"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.path.join(os.environ['HOME'], 'Downloads')
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_blades.append(
                Blade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
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
                    link_fandom=item.get("Link Blades") if item.get("Link Blades") != "N/A" else "",
                )
            )
        else:
            django_blades.append(
                Blade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    link_fandom=item.get("Link Blades") if item.get("Link Blades") != "N/A" else "",
                )
            )

    for item in beyblades_parts.get("Ratchets"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.environ['HOME'] +  '/Downloads'
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_ratchets.append(
                Ratchet(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    type_bey=item.get("Type"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    link_fandom=item.get("Link Ratchets") if item.get("Link Ratchets") != "N/A" else "",
                )
            )
        else:
            django_ratchets.append(
                Ratchet(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    type_bey=item.get("Type"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    link_fandom=item.get("Link Ratchets") if item.get("Link Ratchets") != "N/A" else "",
                )
            )

    for item in beyblades_parts.get("Bits"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.environ['HOME'] +  '/Downloads'
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_bits.append(
                Bit(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    type_bey=item.get("Type"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    stat_burst=item.get("BurstResistanceStat") if item.get("BurstResistanceStat") != "N/A" else None,
                    stat_dash=item.get("DashStat") if item.get("DashStat") != "N/A" else None,
                    link_fandom=item.get("Link Bits") if item.get("Link Bits") != "N/A" else "",
                )
            )
        else:
            django_bits.append(
                Bit(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    type_bey=item.get("Type"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    stat_attack=item.get("AttackStat") if item.get("AttackStat") != "N/A" else None,
                    stat_defense=item.get("DefenseStat") if item.get("DefenseStat") != "N/A" else None,
                    stat_stamina=item.get("StaminaStat") if item.get("StaminaStat") != "N/A" else None,
                    stat_burst=item.get("BurstResistanceStat") if item.get("BurstResistanceStat") != "N/A" else None,
                    stat_dash=item.get("DashStat") if item.get("DashStat") != "N/A" else None,
                    link_fandom=item.get("Link Bits") if item.get("Link Bits") != "N/A" else "",
                )
            )

    for item in beyblades_parts.get("Lock Chips"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.environ['HOME'] +  '/Downloads'
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_lock_chips.append(
                LockChip(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Lock Chips") if item.get("Link Lock Chips") != "N/A" else "",
                )
            )
        else:
            django_lock_chips.append(
                LockChip(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Lock Chips") if item.get("Link Lock Chips") != "N/A" else "",
                )
            )


    for item in beyblades_parts.get("Main Blades"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.environ['HOME'] +  '/Downloads'
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_main_blades.append(
                MainBlade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Main Blades") if item.get("Link Main Blades") != "N/A" else "",
                )
            )
        else:
            django_main_blades.append(
                MainBlade(
                    name_takara=item.get("Takara Tomy Name"),
                    name_hasbro=item.get("Hasbro Name"),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Main Blades") if item.get("Link Main Blades") != "N/A" else "",
                )
            )

    for item in beyblades_parts.get("Assist Blades"):

        
        if item.get("Image") != "N/A" and item.get("Image") != "":
            if os.name == 'nt':
                path_download = os.environ["TEMP"]
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            else:
                path_download = os.environ['HOME'] +  '/Downloads'
                path = utils.download_file(item.get("Image"), path_download)
                path = os.path.join(path_download, path)
            file_name = os.path.basename(path)
            file_image = open(path, "rb")
            django_assist_blades.append(
                AssistBlade(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    image=File(
                        file_image,
                        name=file_name,
                    ),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Assist Blades") if item.get("Link Assist Blades") != "N/A" else "",
                )
            )
        else:
            django_assist_blades.append(
                AssistBlade(
                    abbreviation=item.get("Abbr."),
                    name=item.get("Name"),
                    type_bey=item.get("Type"),
                    spin_direction=item.get("SpinDirection"),
                    weight= item.get("Weight") if item.get("Weight") != "N/A" else None,
                    system_bey=item.get("System"),
                    link_fandom=item.get("Link Assist Blades") if item.get("Link Assist Blades") != "N/A" else "",
                )
            )

    if len(django_blades) > 0:
        Blade.objects.bulk_create(django_blades)
        Ratchet.objects.bulk_create(django_ratchets)
        Bit.objects.bulk_create(django_bits)
        LockChip.objects.bulk_create(django_lock_chips)
        MainBlade.objects.bulk_create(django_main_blades)
        AssistBlade.objects.bulk_create(django_assist_blades)
    
