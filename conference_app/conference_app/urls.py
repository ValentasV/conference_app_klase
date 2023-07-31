"""
URL configuration for conference_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings # settings turi būti importuoti būtent iš django.conf
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include( 'django.contrib.auth.urls' ) ),  - Django sukurta  paskyrų forma.
    # Vietoj 'accounts/' galim parašyti ką tik norim pavyzdžiui 'paskyros/'
    path("accounts/", include("django.contrib.auth.urls")),
    path("Konferencijos/", include("Konferencijos.urls")),
    path("Renginiai/", include("Renginiai.urls")),
]

# Kad vartotojas matytų nuotraukas "images" reikia url nurodyti kelią. tam naudojama speciali komanda "static" (ši komanda gražina listą).
# "Static komanda leidža pasiekti bet kokį failą, kuris yra kokiam nors folderyje. Tą mes ir padarėm apačioje nurodėk kelią iki nuotraukų.
# kuomet importuojame setings tai importuojame ne patį setings.py failą bet django.conf  (settings)
# Pirma kreipiamės į url o po to į aplankalą kuriame yra nuotraukos.
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)