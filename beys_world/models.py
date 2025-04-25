from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Blade(models.Model):
    class Meta:
        verbose_name = _("Blade")
        verbose_name_plural = _("Blades")

    name_takara = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Takara Tomy Name")
    )
    name_hasbro = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Hasbro Name")
    )
    image = models.ImageField(
        upload_to="pictures/blades/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    spin_direction = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Spin Direction")
    )
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    stat_attack = models.IntegerField(null=True, blank=True, verbose_name=_("Attack"))
    stat_defense = models.IntegerField(null=True, blank=True, verbose_name=_("Defense"))
    stat_stamina = models.IntegerField(null=True, blank=True, verbose_name=_("Stamina"))
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.name_hasbro


class Ratchet(models.Model):
    class Meta:
        verbose_name = _("Ratchet")
        verbose_name_plural = _("Ratchets")

    abbreviation = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Abbreviation")
    )
    name = models.CharField(max_length=50, default="N/A", verbose_name=_("Name"))
    image = models.ImageField(
        upload_to="pictures/ratchets/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    stat_attack = models.IntegerField(null=True, blank=True, verbose_name=_("Attack"))
    stat_defense = models.IntegerField(null=True, blank=True, verbose_name=_("Defense"))
    stat_stamina = models.IntegerField(null=True, blank=True, verbose_name=_("Stamina"))
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.abbreviation


class Bit(models.Model):
    class Meta:
        verbose_name = _("Bit")
        verbose_name_plural = _("Bits")

    abbreviation = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Abbreviation")
    )
    name = models.CharField(max_length=50, default="N/A", verbose_name=_("Name"))
    image = models.ImageField(
        upload_to="pictures/bits/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    stat_attack = models.IntegerField(null=True, blank=True, verbose_name=_("Attack"))
    stat_defense = models.IntegerField(null=True, blank=True, verbose_name=_("Defense"))
    stat_stamina = models.IntegerField(null=True, blank=True, verbose_name=_("Stamina"))
    stat_burst = models.IntegerField(
        null=True, blank=True, verbose_name=_("Burst Resistance")
    )
    stat_dash = models.IntegerField(null=True, blank=True, verbose_name=_("Dash"))
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.name


class LockChip(models.Model):
    class Meta:
        verbose_name = "Lock Chip"
        verbose_name_plural = "Lock Chips"

    name_takara = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Takara Tomy Name")
    )
    name_hasbro = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Hasbro Name")
    )
    image = models.ImageField(
        upload_to="pictures/lock_chips/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    spin_direction = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Spin Direction")
    )
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.name_hasbro


class MainBlade(models.Model):
    class Meta:
        verbose_name = "Main Blade"
        verbose_name_plural = "Main Blades"

    name_takara = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Takara Tomy Name")
    )
    name_hasbro = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Hasbro Name")
    )
    image = models.ImageField(
        upload_to="pictures/main_blades/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    spin_direction = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Spin Direction")
    )
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.name_hasbro


class AssistBlade(models.Model):
    class Meta:
        verbose_name = "Assist Blade"
        verbose_name_plural = "Assist Blades"

    abbreviation = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Abbreviation")
    )
    name = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Name")
    )
    image = models.ImageField(
        upload_to="pictures/assist_blades/%Y/%m/%d", blank=True, verbose_name=_("Image")
    )
    type_bey = models.CharField(max_length=50, default="N/A", verbose_name=_("Type"))
    spin_direction = models.CharField(
        max_length=50, default="N/A", verbose_name=_("Spin Direction")
    )
    weight = models.FloatField(
        null=True, blank=True, verbose_name=_("Weight"), default=None
    )
    system_bey = models.CharField(
        max_length=50, default="N/A", verbose_name=_("System")
    )
    link_fandom = models.URLField(max_length=100, verbose_name="Link Fandom")
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Created Date")
    )

    def __str__(self):
        return self.name