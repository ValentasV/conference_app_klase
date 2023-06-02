from django.db import models
from Konferencija.models import Konferencija
# Create your models here.
class Renginys(models.Model):
    start_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    visitors = models.IntegerField(default=0)

    Konferencija = models.ForeignKey(Konferencija, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)