from django.contrib import admin
from Renginiai.models import Renginys, KompanijosRegistracija

# Register your models here.
class  KompanijosRegistracijaAdmin(admin.ModelAdmin):
    list_display = ["kompanijos_pavadinimas", "renginys_title", "dalyvių_skaičius"]

    def renginys_title(self, model):
        return f"Renginys: {model.renginys_title}"

admin.site.register(Renginys)
admin.site.register(KompanijosRegistracija, KompanijosRegistracijaAdmin)
# KompanijosRegistracijaAdmin registruojam modelį su naujom reikšmėmis kad matytūsi admine