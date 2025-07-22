from django.db import models

from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nom

class Facture(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='factures')
    date_emission = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='factures')
    description = models.TextField(blank=True)
    payee = models.BooleanField(default=False)

    # ajouter taxes et ttc 

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"


    def montant_ttc(self):
        return self.montant * (1 + self.tva / 100)

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"