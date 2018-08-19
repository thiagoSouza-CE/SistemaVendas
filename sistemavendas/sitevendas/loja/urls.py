from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:product_id>/add', views.addItemOrder, name="add_item"),
    path('<int:pedido_id>/remove', views.finalizeItemOrder, name='remove_item')
]
