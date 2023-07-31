from django.contrib import admin
from Konferencijos.models import Konferencija, Komentaras
from Renginiai.models import Renginys

class RenginysInline(admin.TabularInline): #
    model = Renginys
    extra = 1 # Admino puslapyje vietoj 3 langelių duoda tik vieną.
class KonferencijaAdmin(admin.ModelAdmin): # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["id", "title", "start_date", "end_date"]
    inlines = [RenginysInline] # inlines = yra listas kuriam nurodom ką jam rodyti
# KonferencijaAdmin apima vis1 Konferencijos klasę, o inlines = [RenginysInline] čia nurodom papildomą klasę.
# inlaino metodas - klasė, pavaizduoja kitus susijusius modelius iš kitos klasės tame pačiame konferencijų lange admino puslapyje.
# ( paima modelius iš Renginiai klasės)

admin.site.register(Konferencija, KonferencijaAdmin),
admin.site.register(Komentaras)