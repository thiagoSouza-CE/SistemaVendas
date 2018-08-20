from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from usuarios.models import Perfil
from usuarios.forms import RegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def get_perfil_logado(request):
     return request.user.perfil

class RegisterView(View):
    template_name = 'usuarios/registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            usuario = User.objects.create_user(dados_form['email'], dados_form['email'], dados_form['senha'])            
            perfil = Perfil(nome=dados_form['nome'],
                            telefone=dados_form['telefone'],
                            usuario=usuario)
            perfil.save()
            return redirect('loja:index')
        return render(request, self.template_name, {'form' : form})
