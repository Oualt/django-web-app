from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    nom = forms.CharField(label='Votre nom', max_length=100)
    email = forms.EmailField(label='Votre adresse email')
    message = forms.CharField(label='Votre message', widget=forms.Textarea, max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        #fields = ['name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage'] # on aurait aussi pu écrire " '__all__' " pour tout récupérer directement
        exclude = ['active', 'official_homepage'] # on exclut les champs "active" et "official_homepage" du formulaire

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__' # on récupère tous les champs du modèle Listing
        #exclude = ['sold'] # on exclut le champ "sold" du formulaire
        widgets = { # on ajoute un widget pour le champ "description"
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 20}) # on ajoute un widget Textarea avec 5 lignes et 20 colonnes
        }