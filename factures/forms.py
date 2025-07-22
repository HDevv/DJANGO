from django import forms
from .models import Facture, Categorie

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rendre le champ catégorie non requis dans le formulaire
        self.fields['categorie'].required = False

    def save(self, commit=True):
        facture = super().save(commit=False)

        if not facture.categorie:
            autres, _ = Categorie.objects.get_or_create(nom="Autres")
            facture.categorie = autres

        if commit:
            facture.save()

        return facture
    

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']


