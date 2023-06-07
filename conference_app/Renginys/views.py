from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView

from Renginys.models import Renginys, RenginysRegistration


# Create your views here.
class RenginysDetailView(DetailView):
    model = Renginys
    context_object_name = "renginys"


class RegisterVisitorView(LoginRequiredMixin, View):
    def get(self, request, renginio_id): # renginio_id  pavadinimas turi sutapti su Renginys/url.py kelio pavadinimu
        renginys = get_object_or_404(Renginys, id=renginio_id)


        registraciju_kiekis = RenginysRegistration.objects.filter(
            renginys = renginys, user = request.user).count()

        if registraciju_kiekis > 0:
            return HttpResponse("jūs jau prisiregistravote")


        registration = RenginysRegistration() # Registracijos - prisijungimo išsaugojimas
        registration.renginys = renginys
        registration.user = request.user
        registration.save()

        return redirect(f"/Renginys/{renginio_id}")

        # return HttpResponse(renginys.title)

class UserEventList(View):
    def get(self, request):

        if not request.user.is_authenticated:
            return redirect("login")

        user_events = RenginysRegistration.objects.filter(
            user = request.user
        )


        return render(
            request,
            "Renginys/user_renginiai.html",
            {"object_list": user_events }
        )

