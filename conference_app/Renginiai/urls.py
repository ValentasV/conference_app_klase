from django.urls import path
from Renginiai.views import RenginysDetailView, RegisterVisitorView, UserEventList

urlpatterns = [
    # int   Django tikėsis sveiko skaičiaus   pk pirminis raktas paimtas iš Renginio modelio.
    # kuomet žmogus nueis į  event/2/  suveiks   RenginysDetailView   funkcija
    # 'renginys-detail' šie pavadinimai turi būti unikalus visoje sistemoje. Tarp visų urls.py failų.
    # Kiekvienam “path“ keliui turi būti priskirta vis kita    name=....   reikšmė – pavadinimas.
    path("<int:pk>/", RenginysDetailView.as_view(), name = 'renginys-detail'),
    # name = 'register-visitor' nurodom savo url pavadinimą ir pagal jį Django matys šį ("path") kelią.
    path("register/<int:renginio_id>/", RegisterVisitorView.as_view(), name = 'register-visitor'),
    path("my-renginiai/", UserEventList.as_view(), name = "user-renginiai"),
]