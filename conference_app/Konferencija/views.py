from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Konferencija, Like


# Create your views here.
class KonferencijaListView(ListView): # ListView yra Django biblioteka - klasė kuri viską už mus padaro
    model = Konferencija # nurodom kokį sąrašą jam atvaizduoti pvz Konferencija



class KonferencijaDetailView(DetailView): # # DetailView yra Django biblioteka - klasė kuri viską už mus padaro
    model = Konferencija


class KonferencijaLikeView(View):
    def get(self, request, konferencijos_id):
        if not request.user.is_suthenticated:
            return redirect("login")

        konferencija = get_object_or_404(Konferencija, id = konferencijos_id)

        laiku_kiekis = Like.objects.filter(
            konferencija=konferencija, user=request.user).count()

        if laiku_kiekis > 0:
            return HttpResponse("jūs jau prisiregistravote")

        registration = Like()  # Registracijos - prisijungimo išsaugojimas
        registration.konferencija = konferencija
        registration.user = request.user
        registration.save()
        return redirect("konferencija-detail", konferencijos_id)
