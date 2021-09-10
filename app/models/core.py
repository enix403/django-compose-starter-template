from django.db import models
from . import fields

class BaseModel(models.Model):
    objects: models.Manager
    class Meta:
        abstract = True

class DemoPersonModel(BaseModel):
    class Meta:
        db_table = "tbl_demo_model"

    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = fields.PositiveTinyIntegerField()