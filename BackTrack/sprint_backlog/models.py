from django.db import models

# Create your models here.
class sprint_backlog_item(models.Model):
    PBI=models.IntegerField() #Indicates which PBI this item belongs to (id of the PBI)
    title=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default="pending",blank=True)
    owner=models.CharField(max_length=100, blank=True)
    estimation=models.IntegerField()

    class Meta:
        ordering = ["PBI","estimation"]

class capacity(models.Model):
    capacity=models.IntegerField()