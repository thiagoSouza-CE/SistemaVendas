from django.db import models
from usuarios.models import Perfil

class Product(models.Model):
    name = models.CharField(max_length=200)
    specification = models.CharField(max_length=200)
    price = models.FloatField()
    CATEGORY_CHOICES = (
        ('PRC', 'Processadores'),
        ('M.R', 'Memória Ram'),
        ('D.R', 'Disco Rígido/SSD'),
        ('P.V', 'Placa de Vídeo'),
        ('GBT', 'Gabinete'),
        ('P.M', 'Placa Mãe'),
        ('F.T', 'Fonte'),
    )
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
    client = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    order_date = models.DateTimeField('data emissão')
    CATEGORY_CHOICES = (
        ('DIN', 'Dinheiro'),
        ('CHE', 'Cheque'),
        ('CTC', 'Cartão de Crédito'),
        ('CTD', 'Cartão de Débito'),
    )

    def __str__(self):
        return str("{}-{}").format(self.client.nome, self.order_date)

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    qtde = models.PositiveIntegerField()

    def total(self):
        return self.price * self.qtde
    
    def __str__(self):
        return str("{}-{}").format(self.product.name, self.qtde)

