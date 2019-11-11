from django.db import models

# Create your models here.
class sprint_backlog_item(models.Model):
    PBI=models.IntegerField() #Indicates which PBI this item belongs to (id of the PBI)
    title=models.CharField(max_length=100)
    # Set the choices of status of PBI. (actual value, readable name)
    sprintItemStatusChoices = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Finished", "Finished"),
        ("Unfinished", "Unfinished")
    ]
    status=models.CharField(max_length=100, choices=sprintItemStatusChoices,default="Pending")
    owner=models.CharField(max_length=100, blank=True)
    estimation=models.IntegerField()

    class Meta:
        ordering = ["PBI","-status", "estimation"]
