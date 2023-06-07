from Konferencija.views import KonferencijaListView, KonferencijaDetailView, KonferencijaLikeView
from django.urls import path

urlpatterns = [ # čia yra nurodomi keliai į klases iš views.py filo
    path("", KonferencijaListView.as_view()),
    path("<int:pk>/", KonferencijaDetailView.as_view(), name = "conference-detail"),
    path("like/<int:konferencijos_id>/", KonferencijaLikeView.as_view(), name = "konferencija-like"),

]

