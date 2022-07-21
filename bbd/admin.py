from django.contrib import admin

from . import models

admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.Skill)
admin.site.register(models.Record)
admin.site.register(models.Season)
admin.site.register(models.Game)