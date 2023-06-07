from django.contrib.auth.models import User
from django.db import models
from Konferencija.models import Konferencija
# Create your models here.
class Renginys(models.Model):
    start_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    # TODO : ištrimti ateityje
    visitors = models.IntegerField(default=0)
# Visi models laukeliai turi defoltines  automatines reikšmes  default = 0
    # bet mes jeigu norime galime tas reikšmes pakeisti ir įrašyti savo reikšmę.


    Konferencija = models.ForeignKey(Konferencija, on_delete=models.CASCADE)
# conference = models.ForeignKey( Conference, on_delete = models.CASCADE ) čia yra tėvinis raktas nurodantis į konferencijos appsą.
# CASCADE nurodo, kad kaip ištrinsime konferenciją, kuriai priklauso šitas renginys tada išsitrins ir šitas renginys.
# (ištrink renginį, kaip ištrinsi tėvinę konferenciją kuriai priklauso šis renginys).
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RenginysRegistration(models.Model):
    renginys = models.ForeignKey( Renginys, on_delete= models.CASCADE)
    # galima sukurti savo susiejimo vardą related_name="registracijos"
    # jis bus susietas su renginys_detail.html  (renginys.registration_set.count)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)