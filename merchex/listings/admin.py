from django.contrib import admin
from listings.models import Band

class BandAdmin(admin.ModelAdmin):  # nous créons une classe BandAdmin
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous enregistrons la classe BandAdmin avec le modèle Band

# Register your models here.
