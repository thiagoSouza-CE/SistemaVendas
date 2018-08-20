from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from .models import Product, Order, ItemOrder, Stock
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime


class IndexView(View):
    template_name = 'loja/loja.html'

    def openOrder(self, perfil):
        last_order_open = Order.objects.filter(client=perfil, status_order='P.A')
        if len(last_order_open) == 0:
            current_client = perfil
            current_order = Order(client=current_client, order_date=datetime.now())
            current_order.save()
            return current_order
        else:
            return last_order_open.first

    def get(self, request):
        list_product = Product.objects.filter()
        context = {'list_product': list_product}
        if(request.user.is_authenticated):
            perfil = request.user.perfil
            opened_order = self.openOrder(perfil)
            last_order_open = Order.objects.filter(client=perfil, status_order='P.A')
            selected_order = ItemOrder.objects.filter(order__in=last_order_open).values_list('product', flat=True)
            context['perfil'] = perfil
            context['order'] = opened_order
            context['itens_order'] = selected_order
        return render(request, self.template_name, context)


class AddView(View):
    template_name = 'loja/add.html'

    def openOrder(self, perfil):
        last_order_open = Order.objects.filter(client=perfil, status_order='P.A')
        if len(last_order_open) == 0:
            current_client = perfil
            current_order = Order(client=current_client, order_date=datetime.now())
            current_order.save()
            return current_order
        else:
            return last_order_open.first

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, product_id, order_id):
        perfil = request.user.perfil
        opened_order = self.openOrder(perfil)
        product = Product.objects.get(pk=product_id)
        stock = Stock.objects.get(product=product)
        context = {
            'product': product,
            'order': opened_order,
            'stock': stock,
            'perfil': perfil
        }
        return render(request, self.template_name, context)

    def post(self, request, product_id, order_id):
        opened_order = Order.objects.get(pk=order_id)
        product = Product.objects.get(pk=product_id)
        newItem = ItemOrder.objects.create(order=opened_order, product=product, 
                                           price=product.price, qtde=1)
        stock = Stock.objects.get(product=product)
        stock.total = stock.total - newItem.qtde
        stock.save()
        newItem.save()
        return redirect('loja:index')
   

class RemoveView(View):
    template_name = 'loja/delete.html'

    def openOrder(self, perfil):
        last_order_open = Order.objects.filter(client=perfil, status_order='P.A')
        if len(last_order_open) == 0:
            current_client = perfil
            current_order = Order(client=current_client, order_date=datetime.now())
            current_order.save()
            return current_order
        else:
            return last_order_open.first
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, product_id, order_id):
        perfil = request.user.perfil
        opened_order = self.openOrder(perfil)
        product = Product.objects.get(pk=product_id)
        context = {
            'product': product,
            'order': opened_order,
            'perfil': perfil
        }
        return render(request, self.template_name, context)

    def post(self, request, product_id, order_id):
        delete_item = ItemOrder.objects.get(order__id=order_id, product__id=product_id)
        product = Product.objects.get(pk=product_id)
        stock = Stock.objects.get(product=product)
        stock.total = stock.total + delete_item.qtde
        stock.save()
        delete_item.delete()
        return redirect('loja:index')
  

class OrderView(View):
    template_name = 'loja/order.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, perfil_id):
        perfil = request.user.perfil
        list_order = Order.objects.filter(client__id = perfil_id)
        context = {
            'perfil': perfil,
            'list_order': list_order
        }
        return render(request, self.template_name, context)
    
    def post(self, request, perfil_id):
        finalize_order = Order.objects.filter(client__id = perfil_id, status_order='P.A').update(status_order='P.R')
        return redirect('loja:index')


@login_required
def finalizeItemOrder(request, pedido_id):
    perfil = request.user.perfil
    return HttpResponse("Finalizando Item %s" % pedido_id)
