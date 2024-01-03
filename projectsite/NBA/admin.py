from django.contrib import admin
from .models import NBATeam,NBAPlayer,Playerscareer,Brands,ProLeague

@admin.register(NBATeam)
class NBAAdmin(admin.ModelAdmin):
    list_display = ("name", "years_active","league",)
    search_fields = ("name",)
    
@admin.register(NBAPlayer)
class NBAAdmin(admin.ModelAdmin):
    list_display = ("name","birthdate","college",)
    search_fields = ("name",)

@admin.register(Playerscareer)
class NBAAdmin(admin.ModelAdmin):
    list_display = ("Player","Team","Seasons","Income","Brand",)
    search_fields = ("Player",)

@admin.register(Brands)
class NBAAdmin(admin.ModelAdmin):
    list_display = ("brand_name","email",)
    search_fields = ("brand_name",)
    
class ProLeague(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
