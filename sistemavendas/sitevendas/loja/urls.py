from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:product_id>/<int:order_id>/add', views.AddView.as_view(), name="add_item"),
    path('<int:product_id>/<int:order_id>/remove', views.RemoveView.as_view(), name='remove_item'),
    path('<int:perfil_id>/order', views.OrderView.as_view(), name='list_order')
]
