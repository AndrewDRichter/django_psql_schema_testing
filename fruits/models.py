from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fruit(BaseModel):
    name = models.CharField(max_length=100)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = '"coreschema"."fruit"'


class Vegetable(BaseModel):
    name = models.CharField(max_length=100)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
