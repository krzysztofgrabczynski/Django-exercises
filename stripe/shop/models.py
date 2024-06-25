from django.db import models

class TestOrder(models.Model):
    amount = models.PositiveSmallIntegerField(null=True)
    
class TestProduct(models.Model):
    name = models.CharField(max_length=32, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    order = models.ForeignKey(TestOrder, null=True, on_delete=models.CASCADE, related_name="products")


