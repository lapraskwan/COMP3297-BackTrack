from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.IntegerField()

#class PB_item(model.Model):
#    feature=models.models.CharField(max_length=100)
#    Status=models.CharField(max_length=100)
#    priority=models.IntegerField()
#    story_point=models.IntegerField(default=1)
