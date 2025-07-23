from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

# CLIENT
class Client(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nom

# FORMULAIRE FACTURES     
class FactureManager(models.Manager):
    def get_queryset(self):
        return FactureQuerySet(self.model, using=self._db)

    def payees(self):
        return self.get_queryset().payees()

    def non_payees(self):
        return self.get_queryset().non_payees()

    def pour_client(self, client_id):
        return self.get_queryset().pour_client(client_id)

# FACTURE 
class Facture(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='factures')
    date_emission = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='factures')
    description = models.TextField(blank=True)
    payee = models.BooleanField(default=False)
    objects = FactureManager() 

    # ajouter taxes et ttc 

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"


    def montant_ttc(self):
        return self.montant * (1 + self.tva / 100)

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"
    

# MIDDLEWARE 
class FactureLog(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='logs')
    created_at = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)  # l’URL appelée
    user_agent = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"Log de création pour {self.facture} à {self.created_at}"

# QUERY SET 
class FactureQuerySet(models.QuerySet):
    def payees(self):
        return self.filter(payee=True)

    def non_payees(self):
        return self.filter(payee=False)

    def pour_client(self, client_id):
        return self.filter(client__id=client_id)
    

