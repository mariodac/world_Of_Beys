from django.contrib import admin

from beys_world import models


@admin.register(models.Blade)
class BladeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_takara",
        "name_hasbro",
        "type_bey",
        "spin_direction",
        "weight",
        "system_bey",
        "stat_attack",
        "stat_defense",
        "stat_stamina",
        "link_fandom",
        "created_date",
        "show",
    )
    ordering = (
        "name_hasbro",
        "name_takara",
        "stat_attack",
        "stat_defense",
        "stat_stamina",
    )
    list_filter = ("type_bey", "system_bey", "created_date", "show")
    search_fields = ("name_takara", "name_hasbro")
    list_per_page = 10
    list_max_show_all = 100
    list_editable = (
        "name_takara",
        "name_hasbro",
        "type_bey",
        "spin_direction",
        "weight",
        "system_bey",
        "stat_attack",
        "stat_defense",
        "stat_stamina",
        "link_fandom",
        "show",
    )
    list_display_links = ("id",)

@admin.register(models.Ratchet)
class RatchetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "abbreviation",
        "name",
        "image",
        "type_bey",
        "weight",
        "system_bey",
        "stat_attack",
        "stat_defense",
        "stat_stamina",
        "link_fandom",
        "show",
        "created_date",
    )
    ordering = ("abbreviation", "name", "stat_attack", "stat_defense", "stat_stamina")
    list_filter = ("type_bey", "system_bey", "created_date", "show")
    search_fields = ("abbreviation", "name")
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ("id",)

@admin.register(models.Bit)
class BitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "abbreviation",
        "name",
        "image",
        "type_bey",
        "weight",
        "system_bey",
        "stat_attack",
        "stat_defense",
        "stat_stamina",
        "stat_burst",
        "stat_dash",
        "link_fandom",
        "show",
        "created_date",
    )
    ordering = ("abbreviation", "name", "stat_attack", "stat_defense", "stat_stamina")
    list_filter = ("type_bey", "system_bey", "created_date", "show")
    search_fields = ("abbreviation", "name")
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ("id",)


@admin.register(models.LockChip)
class LockChipAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_takara",
        "name_hasbro",
        "image",
        "spin_direction",
        "weight",
        "system_bey",
        "link_fandom",
        "show",
        "created_date",
    )
    ordering = ("name_hasbro", "name_takara")
    list_filter = ("created_date", "show")
    search_fields = ("name_takara", "name_hasbro")
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ("id",)

@admin.register(models.MainBlade)
class MainBladeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_takara",
        "name_hasbro",
        "image",
        "spin_direction",
        "weight",
        "system_bey",
        "link_fandom",
        "show",
        "created_date",
    )
    ordering = ("name_hasbro", "name_takara")
    list_filter = ("created_date", "show")
    search_fields = ("name_takara", "name_hasbro")
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ("id",)

@admin.register(models.AssistBlade)
class AssistBladeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "abbreviation",
        "name",
        "image",
        "spin_direction",
        "weight",
        "system_bey",
        "link_fandom",
        "show",
        "created_date",
    )
    ordering = ("abbreviation", "name")
    list_filter = ("created_date", "show")
    search_fields = ("abbreviation", "name")
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ("id",)
