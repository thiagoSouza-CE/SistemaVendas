from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    
    @property
    def email(self):
        return self.usuario.email
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")

    def get_perfil_logado(request):
        return Perfil.objects.get(id=1)

