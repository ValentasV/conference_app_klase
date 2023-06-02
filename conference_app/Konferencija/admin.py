from django.contrib import admin
from Konferencija.models import Konferencija
from Renginys.models import Renginys

class RenginysInline(admin.TabularInline):
    model = Renginys
class KonferencijaAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "start_date", "end_date"]
    inlines = [RenginysInline]


admin.site.register(Konferencija, KonferencijaAdmin)