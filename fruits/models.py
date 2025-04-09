from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fruit(BaseModel):
    name = models.CharField(max_length=100)
    # market_value = models.
    
    class Meta:
        db_table = '"coreschema"."fruit"'
