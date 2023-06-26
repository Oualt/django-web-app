from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id) # obtenir l'objet Band qui a l'id passé en paramètre
    return render(request, 'listings/band_detail.html', {'band': band}) # on passe l'objet Band à la vue

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST) # créer un formulaire BandForm avec les données POST
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band) # créer et remplir le formulaire avec les données de l'instance Band
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm(instance=band)

    return render(request,
            'listings/band_change.html',
            {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes avec un message flash
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuer simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST) # créer un formulaire ListingForm avec les données POST
        if form.is_valid():
            # créer une nouvelle « Listing » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>Nous adorons Merch !</p>')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["nom"] or "anonyme"} via Merchex', # nom = nom dans le formulaire form.py
                message=form.cleaned_data['message'], # message = message dans le formulaire form.py
                from_email=form.cleaned_data['email'], # email = email dans le formulaire form.py
                recipient_list=['admin@merchex.xyz'],) # mail où on reçoit le message
        return redirect('email-envoye')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

def email_envoye(request):
    return render(request, 'listings/email_envoye.html')