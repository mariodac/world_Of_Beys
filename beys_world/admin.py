from django.contrib import admin

from beys_world import models


@admin.register(models.Blade)
class BladeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_takara",
        "name_Hasbro",
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
    ordering = ("name_Hasbro", "name_takara", "stat_attack", "stat_defense", "stat_stamina")
    list_filter = ("type_bey", "system_bey", "created_date", "show")
    search_fields = ("name_takara", "name_Hasbro")
    list_per_page = 10
    list_max_show_all = 100
    list_editable = (
        "name_takara",
        "name_Hasbro",
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
    list_display_links = (
        "id",
    )
