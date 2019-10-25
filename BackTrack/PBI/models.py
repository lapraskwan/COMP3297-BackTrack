from django.db import models

# Create your models here.
class PB_item(models.Model):
    feature=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default="pending",blank=True)
    priority=models.IntegerField()
    story_point=models.IntegerField(default=1,)
