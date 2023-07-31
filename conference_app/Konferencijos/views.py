from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Konferencija, Like, Komentaras
from datetime import datetime

# Create your views here.
class KonferencijaListView(ListView): # ListView yra Django biblioteka - klasė kuri viską už mus padaro
    model = Konferencija # nurodom kokį sąrašą jam atvaizduoti pvz Konferencijos
# model = Konferencijos  yra lygus  konferencija_list.html,  kuris keliauja į html ir virsta  object_list (konferencija paverčia mažosiom raidėm.)
# ListView klasė pagal pateiktą modelį Konferencijos (modelis =Konferencijos) ieško templeito (konferencija_list.html)
# Kadangi konferencijos modelis turi start_date, end_date , tittle,  mes juos galim išimti konferencija_list.html file
# parašę {{ konferencija.title }} ({{ konferencija.start_date }} - {{ konferencija.end_date }}) Django vietoj šitų skliaustų įrašys paduodamas reikšmes (Vartotojo) iš duomenų bazės.
# ListView – duoda visas konferencijas
# ListView, kuomet mes parašome model = Konferencijos
#   vykdo šią funkciją  Konferencijos.objects.all() – pasirenka savo viduje visus modelio objektus
# o išsikviečia per object  komandą. konferencija_detail.html  faile.
# Galime tuos objektus išsikviesti ir perfiltruoti pvz:
# queryset = Konferencijos.objects.order_by(“start_date”) sugrupuos pagal pradžios datą. (“-start_date”) jeigu parašysim priekį minusą sugrupuos atvirkščiai.
# Vietoj to kad viską paimtu galime prafiltruoti kad išsimtų būtent vieną objektą ar kelis kuriuos mes norime
# Parašant       queryset = Konferencijos.objects.filter(……)


class KonferencijaDetailView(DetailView): # # DetailView yra Django biblioteka - klasė kuri viską už mus padaro
    model = Konferencija
# class KonferencijaDetailView( DetailView ):  kuomet mes iškviesime Detail view klasę duosime elementą
# object_ - konferencija_detail.html
# DetailView – duoda daaugiau detalių iš vienos konferencijos



class KonferencijaLikeView(View):
    def get(self, request, konferencijos_id):
        if not request.user.is_authenticated:
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



class SukurtiKomentaroView(View, LoginRequiredMixin):

    def post(self, request, konferencijos_id): #  konferencijos_id -> turi sutapti su pavadinimu urls.py faile!
       #  return HttpResponse("Funkcija veikia", {konferencijos_id}) PASITIKRINIMUI AR VEIKIA
    # 1. Išsitraukti visas reikšmes
        komentaro_tekstas = request.POST.get("komentaras")
    # 2.Validacija
        if len(komentaro_tekstas) == 0:
            messages.error(request, "Komentaras negali būti tuščias")
            return redirect(f"/konferencijos/{konferencijos_id}")

       # tikriname ar vartotojas yra prisijungęs
       # if request.user.is_authenticated == False:
       #     return HttpResponse( "Klaida! Jums reikia prisijungti" )

       # Jeigu naudojam šią funkciją LoginRequiredMixin  nereikia tikrinti ar vartotojas yra prisijungęs


       # Vienu metu patikriname, ar yra konferencija su konferencijos_id, ir
       # taip pat išsaugome Conference objektą su tuo konferencijos_id
        konferencija = get_object_or_404(Konferencija, id=konferencijos_id)

    # 3. Veiksmas - Įrašyti komentąrą į duomenų bazę
        komentaras = Komentaras()
        komentaras.autorius = request.user
        komentaras.komentaras = komentaro_tekstas
        komentaras.konferencija = konferencija
        komentaras.save()

    # 4. Rezultatas vartotojui
        return redirect(f"/konferencijos/{konferencijos_id}")

class SusikurkimeKonferencijosView(View):
    def get(self, request):
        return render(
            request,
            "Konferencijos/konferencija_create.html"

        )

    def post(self, request):

        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        title = request.POST.get("title")

        if len(title) == 0:
            messages.error(request, "Būtina įvesti pavadinimą")
            return redirect("/konferencijos/new")
        try:

            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messages.error(request, "Būtina įvesti pavadinimą")
            return redirect("/konferencijos/new")


        # 2. Viksmas - sukurimame įeašą.

        konferencija = Konferencija()
        konferencija.start_date = start_date
        konferencija.end_date = end_date
        konferencija.title = title
        konferencija.save()


        # 3. Išsivedam rezultatą
        return redirect(f"/Konferencijos/{konferencija.id}/")