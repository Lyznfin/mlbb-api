from django.contrib import admin
from .models import Hero, Lane, Speciality, Role, HeroRatings

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('hero_name', 'hero_alias', 'roles', 'specialities', 'lanes')
    prepopulated_fields = {"hero_slug": ("hero_name","hero_alias")}

@admin.register(HeroRatings)
class HeroRatingsAdmin(admin.ModelAdmin):
    list_display = ('hero', 'durability', 'offense', 'control_effects', 'difficulty')

admin.site.register(Lane)
admin.site.register(Speciality)
admin.site.register(Role)