from .views import KonferencijaListView, KonferencijaDetailView, KonferencijaLikeView, SukurtiKomentaroView, SusikurkimeKonferencijosView
from django.urls import path

urlpatterns = [ # čia yra nurodomi keliai į klases iš views.py filo
    path("", KonferencijaListView.as_view()),
    # path( "<int:pk>/", KonferencijaDetailView.as_view(), name = "conference-detail"  Bet koks skaičius kurį įrašysim į <int> vietą atitiks šitą kelią.
    # <int:pk>  (int – integer (sveikas skaičius)   pk – primary key (pirminis raktas) šitas kelias atitinka /Konferencijos/1/.../Konferencijos/2/.... ir t.t.
    # neaišku argalima filtruoti ir pagal stringą ir pavadinimą <str:title>
    path("<int:pk>/", KonferencijaDetailView.as_view(), name = "konferencija-detail"),
    path("like/<int:konferencijos_id>/", KonferencijaLikeView.as_view(), name="konferencija-like"),
    path("<int:konferencijos_id>/komentarai/", SukurtiKomentaroView.as_view(), name="sukurti_komentarą"),
    path("new/", SusikurkimeKonferencijosView.as_view(), name = "konferencija-sukurkime"),

]

