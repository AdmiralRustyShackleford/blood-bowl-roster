from django.db import models
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    name = models.TextField(default='Skill Name')
    description = models.TextField(default='Skill description')


class Team(models.Model):
    class TeamType(models.TextChoices):
        BLACK_ORC = 'BO', _('Black Orc')
        CHAOS_CHOSEN = 'CC', _('Chaos Chosen')
        CHAOS_RENEGADES = 'CR', _('Chaos Renegades')
        DARK_ELF = 'DE', _('Dark Elf')
        DWARF = 'DW', _('Dwarf')
        ELVEN_UNION = 'EU', _('Elven Union')
        GOBLIN_MODE = 'GM', _('Goblin')
        HALFLING = 'HA', _('Halfling')
        HUGH_MANN = 'HM', _('Human')
        IMPERIAL_NOBILITY = 'IN', _('Imperial Nobility')
        LIZARDMEN = 'LZ', _('Lizardmen')
        NECROMANTIC_HORROR = 'NH', _('Necromantic Horror')
        NURGLE = 'NU', _('Nurgle')
        OGRE = 'OG', _('Ogre')
        OLD_WORLD_ALLIANCE = "OW", _('Old World ALliance')
        ORC = 'OR', _('Orc')
        SHAMBLING_UNDEAD = 'SU', _('Shambling Undead')
        SKAVEN = 'SK', _('Skaven')
        SNOTLING = 'SN', _('Snolting')
        UNDERWORLD_DENIZENS = 'UD', _('Underworld Denizens')
        WOOD_ELF = 'WE', _('Wood Elf')

    team_type = models.CharField(
        max_length=2,
        choices=TeamType.choices,
        default=TeamType.BLACK_ORC,
    )
    name = models.CharField(max_length=200)
    primary_color = models.CharField
    secondary_color = models.CharField
    coach_name = models.CharField(max_length=200)
    fans = models.IntegerField
    touchdowns = models.IntegerField
    casualties = models.IntegerField
    league_points = models.IntegerField
    rerolls = models.IntegerField
    asst_coaches = models.IntegerField
    cheerleaders = models.IntegerField
    apothecary = models.IntegerField
    team_value = models.IntegerField
    current_value = models.IntegerField
    division = models.CharField


class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    number = models.IntegerField
    MA = models.IntegerField
    ST = models.IntegerField
    AG = models.IntegerField
    AV = models.IntegerField
    skills = models.ManyToManyField(Skill)
    team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL,
    )
    position = models.CharField(max_length=50)
    spp = models.IntegerField

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class Record(models.Model):
    wins = models.IntegerField
    losses = models.IntegerField
    draws = models.IntegerField
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True, )


class Season(models.Model):
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)


class Game(models.Model):
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
    )
    opponent = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    fan_factor = models.IntegerField
    petty_cash = models.IntegerField
    inducements = models.CharField(max_length=250)
    current_value = models.IntegerField
    RESULT_WIN = 'W'
    RESULT_LOSS = 'L'
    RESULT_DRAW = 'D'
    RESULT_CHOICES = [
        (RESULT_WIN, 'Win'),
        (RESULT_LOSS, 'Loss'),
        (RESULT_DRAW, 'Draw'),
    ]
    result = models.CharField(
        max_length=4,
        choices=RESULT_CHOICES,
    )
    score = models.IntegerField
    league_points = models.IntegerField
    notes = models.TextField
