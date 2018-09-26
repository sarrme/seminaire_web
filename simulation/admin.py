from django.contrib import admin

from .models import Entreprise, Activite, Commentaire
admin.site.register(Entreprise)
admin.site.register(Activite)
admin.site.register(Commentaire)
