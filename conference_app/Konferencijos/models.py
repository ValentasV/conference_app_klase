from django.contrib.auth.models import User
from django.db import models
# Jeigu kažką keičiam models.py tada turim daryti migracijas nes keičiasi informacija duomenų bazėse.
# Create your models here.
class Konferencija(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)

# kad galėtumėme naudotis nuotraukų modeliu turim instaliuotis pillow (pip install pillow)
    picture = models.ImageField( blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    # created_at =  skirtas administratoriams, pasižiūrėti kada kas buvo sukurtas, patobulintas ar sugadintas modelis
    # auto_now_add = True  šia dalis skliausteliuose  nurodo, kad kaip sukursim įrašą konferencijos klasėje esančiame bet kurimame modelyje automatiškai susikurs ir funkcija created_at   (data)
    updated_at = models.DateTimeField(auto_now=True) # Kiekvieną kartą atnaujinus bet kurį modelį rodys dabartinę datą.


    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    konferencija = models.ForeignKey(Konferencija, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

class Komentaras(models.Model):
    autorius = models.ForeignKey(User, on_delete = models.CASCADE)
    komentaras = models.TextField()
    konferencija = models.ForeignKey(Konferencija, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)