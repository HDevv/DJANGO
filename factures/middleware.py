from django.utils.deprecation import MiddlewareMixin
from .models import Facture, FactureLog

class LogFactureCreationMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == "POST" and request.path == "/facture/ajouter/":

            # Récupère la dernière facture ajoutée
            facture = Facture.objects.order_by('-id').first()

            # Vérifie si elle a été ajoutée maintenant (pas une redite)
            if facture and not facture.logs.exists():
                FactureLog.objects.create(
                    facture=facture,
                    path=request.path,
                    user_agent=request.META.get('HTTP_USER_AGENT', ''),
                    ip_address=self.get_client_ip(request)
                )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
