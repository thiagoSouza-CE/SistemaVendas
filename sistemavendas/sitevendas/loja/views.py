from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from .models import Product, Order, ItemOrder
from django.contrib.auth.decorators import login_required
from datetime import datetime


class IndexView(View):
    template_name = 'loja/loja.html'
    # use to add item 
    def openOrder(self):
        last_order_open = Order.objects.filter(client=self.request.user.perfil, 
                                                   status_order='P.A')
        if len(last_order_open) == 0:
            current_client = self.request.user.perfil
            last_order_open = Order.objects.filter(client=current_client, status_order='P.A')
            current_order = Order(client=current_client, order_date=datetime.now())
            current_order.save()
        return 

    def get(self, request):
        list_product = Product.objects.all()
        context = {'list_product': list_product}
        if(request.user.is_authenticated):
            context['perfil'] = request.user.perfil
        return render(request, self.template_name, context)

@login_required
def addItemOrder(request, product_id):
    return HttpResponse("Add Item %s" % product_id)

@login_required
def removeItemOrder(request, product_id):
    return HttpResponse("Add Item %s" % product_id)

@login_required
def finalizeItemOrder(request, pedido_id):
    return HttpResponse("Remova Item %s" % pedido_id)

def get_perfil_logado(request):
     return request.user.perfil