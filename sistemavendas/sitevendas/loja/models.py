from django.db import models

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
        return str(self.total)
