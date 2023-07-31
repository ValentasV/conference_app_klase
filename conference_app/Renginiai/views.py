from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from Renginiai.models import Renginys, RenginysRegistration, KompanijosRegistracija


# class RenginysDetailView( DetailView ): turi savyje get funkciją kuri mums suveikia ir iškviečia šią užklausą
# <form action="{% url 'renginys-detail' renginys.id %}" method="post">
class RenginysDetailView(DetailView):
    model = Renginys
    context_object_name = "renginys" # pakeičiam "object" kintamojo html faile pavadinimą į mums patinkamą. (renginys)


    # def post(self, request, pk):  # pk ateina iš url.py  failo  ir šito kelio
    # path('<int:pk>/', EventDetailView.as_view(), name="event-detail"
    # viskas kas ateina į mūsų serverį turi būti patikrinta.
    # Ar Vartotojas įvedė skaičių, o ne kokią raidę. Ar pk išvis egzistuoja duomenų bazėje ir panašiai.
    def post(self, request, pk):
        # Užduotys
        # Apdoroti request
        # 0. Išsitraukti duomenis į kintamuosius iš models.py failo klasės (nebūtina, bet gera praktika)
        kompanijos_pavadinimas = request.POST.get("Įmonės_pavadinimas")
        Žmonių_skaičius = request.POST.get("Žmonių_skaičius")
        pastaba = request.POST.get("Pastabos")
        # 1. patikrinti vartotojo įvestus duomenis
        # su messages.error vykdomas reik6m4s tikrinimas - vartotojo įvedimas
        if not Žmonių_skaičius.isnumeric():
            messages.error(request, "Žmonių skaičius turi būti skaitinė vertė :(")
            return redirect(f"/Renginiai/{pk}")
        if len(kompanijos_pavadinimas) == 0:
            messages.error(request, "Įmonės pavadinimas turi būti užpildytas")
            return redirect(f"/Renginiai/{pk}")
        # 2. Patikrinti ar pk egzistuoja (ar yta toks Renginiai su primary key)

        # Renginys, pk = pk - pk yra lygiai tas pats kas id(Django duomenų bazėje ieškos pk pagal id)
        renginys = get_object_or_404(Renginys, pk = pk)
        # 3. Veiksmas: įrašymas į duomenų bazę (kursime naują registracija)
        registracija = KompanijosRegistracija()
        registracija.kompanijos_pavadinimas = kompanijos_pavadinimas
        registracija.dalyvių_skaičius = Žmonių_skaičius
        registracija.pastabos = pastaba
        registracija.renginys = renginys
        registracija.save() # funkcija save() yra paimama iš Django base.py failo (Django funkcija).
        # 4. Rezultatas: HTML arba redirect

        # gražinimas į pradinį tinklapio puslapį.
        return redirect(f"/Renginiai/{pk}")



# Mixin yra klasė iš kurio paveldime Django funkciją. šiuo atveju LoginRequired
# LoginRequiredMixin ši funkcija nurodo jeigu vartotojas neprisijunges jis bus automatiškai nukreiptas į login langą.
class RegisterVisitorView(LoginRequiredMixin, View):
    # renginio_id ateina iš url.py failo
    def get(self, request, renginio_id): # renginio_id  pavadinimas turi sutapti su Renginiai/url.py kelio pavadinimu
        # get_object_or_404  ši funkcija mėgins gauti objektą pagal kažkokį kriterijų arba išmes 404 klaidą
        # Skliausteliuose nurodom  kokį objektą norim gauti. Toliau įrašę objektą, nurodom pagal ką jį filtruosim
        # filtracija vyks pagal id  žmogui įvedus skaičių pagal url faile nurodytą kelią, kurį taip pat nurodom id=renginio_id
        # Jeigu neranda sukurto renginio pagal skaičių išmes klaidą 404
        renginys = get_object_or_404(Renginys, id=renginio_id)
        #  galime skaičiuoti kiek lankytojų apsilanko mūsų puslapyje parašant renginys.visitors += 1 reik6m4 saugoma tik kompiuterio atmintyje
        # įvedus paapildonmai renginys.save()
        # renginys.visitors += 1
        # renginys.save()
        # return HttpResponse(renginys.title) arba
        # return redirect(f"/Renginiai/{renginio_id"} redirect funkcija atgal gražina į mūsų nurodyta url (puslapį)



        registraciju_kiekis = RenginysRegistration.objects.filter(
            renginys = renginys, user = request.user).count()
        # žmogui leidžiama prisiregistruoti tik vieną kartą, kitu atveju išveda return išraišką.
        if registraciju_kiekis > 0:
            return HttpResponse("jūs jau prisiregistravote")


        # kol kas registracija yra dar tuščia
        registration = RenginysRegistration() # Registracijos - prisijungimo išsaugojimas
        # viskas paimta iš    class  RenginysRegistration
        # priskiriams renginį
        registration.renginys = renginys
        # priskiriam vartotoją kuris užsiregistruoja
        registration.user = request.user
        # Toliau su save() viskas išsaugoma duomenų bazėje
        registration.save()

        return redirect(f"/Renginiai/{renginio_id}")

        # return HttpResponse(renginys.title)

class UserEventList(View):
    def get(self, request):
        # Apsauga nuo neprisijungusių vartotojų. Neprisijungusius nukreipia į "login" puslapį.
        if not request.user.is_authenticated:
            return redirect("login")
        # Prafiltruoja visą duomenų bazę pagal "user" (userio modelį)
        user_renginiai = RenginysRegistration.objects.filter(
            user = request.user
        )


        return render(
            request,
            "Renginiai/user_renginiai.html",
            {"object_list": user_renginiai }
        )

