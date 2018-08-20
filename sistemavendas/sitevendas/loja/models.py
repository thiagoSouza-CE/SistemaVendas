from django.db import models
from usuarios.models import Perfil


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('PRC', 'Processadores'),
        ('M.R', 'Memória Ram'),
        ('D.R', 'Disco Rígido/SSD'),
        ('P.V', 'Placa de Vídeo'),
        ('GBT', 'Gabinete'),
        ('P.M', 'Placa Mãe'),
        ('F.T', 'Fonte'),
    )
    name = models.CharField(max_length=200)
    specification = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(
        max_length = 3,
        choices = CATEGORY_CHOICES,
    )
    
    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str("{}-{}").format(self.product.name, self.total)   

class Order(models.Model):
    STATUS_CHOICES = (
        ('P.A', 'Pedido Aberto'),
        ('P.R', 'Pedido Realizado'),
        ('S.E', 'Separação em Estoque'),
        ('MTG', 'Em montagem'),
        ('R.T', 'Realização de testes'),
    )
    client = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    order_date = models.DateTimeField('data emissão')
    status_order = models.CharField(
        max_length = 3,
        choices = STATUS_CHOICES,
        default = "P.A"
    )

    @staticmethod
    def returnOpenOrder(perfil):
        last_order_open = Order.objects.filter(client=perfil, status_order='P.A')
        if len(last_order_open) == 0:
            current_client = self.request.user.perfil
            current_order = Order(client=current_client, order_date=datetime.now())
            current_order.save()
            return current_order
        else:
            return last_order_open.first

    def __str__(self):
        return str("{}-{}").format(self.client.nome, self.order_date)

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    qtde = models.PositiveIntegerField()

    def total(self):
        return self.price * self.qtde
    
    def __str__(self):
        return str("{}-{}").format(self.product.name, self.qtde)

class Invoice(models.Model):
    PAYMENT_CHOICES = (
        ('DIN', 'Dinheiro'),
        ('CHE', 'Cheque'),
        ('CTC', 'Cartão de Crédito'),
        ('CTD', 'Cartão de Débito'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(
        max_length = 3,
        choices = PAYMENT_CHOICES,
    )
    price = models.FloatField()

    def __str__(self):
        return str("ID{}-{}").format(self.order.id, self.price)
