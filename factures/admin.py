from django.contrib import admin
from .models import Facture, Client, Categorie

@admin.action(description="Marquer comme payée")
def paid(modeladmin, request, queryset):
    queryset.update(payee=True)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero', 'client', 'montant', 'payee', 'date_emission')
    list_filter = ('client', 'payee', 'categorie')
    search_fields = ('numero', 'client__nom', 'client__email')
    actions = [paid]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')
    search_fields = ('nom', 'email')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
