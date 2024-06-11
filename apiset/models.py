from django.db import models

# app api와 이름이 같은 모델임으로 Product_for_viewset 모델명 변경
class Product_for_viewset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
