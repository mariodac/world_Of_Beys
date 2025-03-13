from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Blade(models.Model):
    class Meta:
        verbose_name = _("Blade")
        verbose_name_plural = _("Blades")

    name_takara = models.CharField(max_length=50, default="N/A", verbose_name=_("Takara Tomy Name"))
    name_Hasbro = models.CharField(max_length=50, default="N/A", verbose_name=_("Hasbro Name"))
    image = models.ImageField(
        upload_to="pictures/blades/%Y/%m/%d",
        blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    spin_direction = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Spin Direction")
    )
    weight = models.FloatField(blank=True, verbose_name=_("Weight"))
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    stat_attack = models.IntegerField(blank=True, verbose_name=_("Attack"))
    stat_defense = models.IntegerField(blank=True, verbose_name=_("Defense"))
    stat_stamina = models.IntegerField(blank=True, verbose_name=_("Stamina"))
    link_fandom = models.CharField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )
