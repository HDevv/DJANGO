from django.test import TestCase
from django.urls import reverse
from .models import Facture, Client, Categorie
from datetime import date

# SETUP 
class BaseFactureTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(nom="Client Test")
        self.categorie = Categorie.objects.create(nom="Services")
        self.facture = Facture.objects.create(
            numero="F123",
            client=self.client_obj,
            date_emission=date.today(),
            montant=100,
            tva=20,
            categorie=self.categorie,
            description="Facture de test",
            payee=False,
        )

# FACTURE LIST 
class FactureListViewTest(BaseFactureTest):
    def test_status_code(self):
        response = self.client.get(reverse('liste_factures'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('liste_factures'))
        self.assertTemplateUsed(response, 'factures/facture_list.html')

    def test_facture_in_context(self):
        response = self.client.get(reverse('liste_factures'))
        self.assertIn(self.facture, response.context['factures'])


# FACTURE DETAIL 
class FactureDetailViewTest(BaseFactureTest):
    def test_status_code(self):
        response = self.client.get(reverse('detail_facture', args=[self.facture.pk]))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('detail_facture', args=[self.facture.pk]))
        self.assertTemplateUsed(response, 'factures/facture_detail.html')

    def test_facture_in_context(self):
        response = self.client.get(reverse('detail_facture', args=[self.facture.pk]))
        self.assertEqual(response.context['facture'], self.facture)


# CREATION DE FACTURE 
class FactureCreateViewTest(BaseFactureTest):
    def test_get_form_page(self):
        response = self.client.get(reverse('creer_facture'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'factures/facture_form.html')

    def test_valid_post_creates_facture(self):
        response = self.client.post(reverse('creer_facture'), {
            'numero': 'F456',
            'client': self.client_obj.pk,
            'date_emission': '2025-07-23',
            'montant': 250,
            'tva': 10,
            'description': 'Création test'
        })
        self.assertEqual(response.status_code, 302)  # redirection
        self.assertTrue(Facture.objects.filter(numero='F456').exists())

    def test_invalid_post_does_not_create(self):
        response = self.client.post(reverse('creer_facture'), {
            'client': self.client_obj.pk,  # pas de 'numero'
            'date_emission': '2025-07-23',
            'montant': 250,
            'tva': 10,
        })
        self.assertEqual(response.status_code, 200)  # form renvoyé
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('numero', form.errors)
