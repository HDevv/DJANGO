from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture, Client
from .forms import FactureForm

# Création
def creer_facture(request):
    form = FactureForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_factures')
    return render(request, 'factures/facture_form.html', {'form': form})

# Modification
def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    form = FactureForm(request.POST or None, instance=facture)
    if form.is_valid():
        form.save()
        return redirect('liste_factures')
    return render(request, 'factures/facture_form.html', {'form': form})

# Suppression
def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'factures/facture_confirm_delete.html', {'facture': facture})

# Affichage d'une facture
def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'factures/facture_detail.html', {'facture': facture})

# Liste des factures
def liste_factures(request):
    client_id = request.GET.get('client')  # chaîne
    clients = Client.objects.all()

    factures = Facture.objects.all()
    if client_id:
        factures = factures.filter(client__id=client_id)

    return render(request, 'factures/facture_list.html', {
        'factures': factures,
        'clients': clients,
        'client_id': client_id,  # str
    })
