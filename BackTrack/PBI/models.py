from django.db import models

# Create your models here.
class PB_item(models.Model):
    #name of this PBI

    class Meta:
        ordering=['priority_no']
    name=models.CharField(max_length=100)
    
    #status of this PBI, e.g. "Finished"
    status=models.CharField(max_length=100,default="Pending",blank=True)
    
    #Priority number of this PBI, i.e. the most important feature has priority 1, the second most has priority 2, etc
    priority_no=models.IntegerField()

    #Story point estimation of this PBI
    story_point=models.IntegerField(default=1)

    #Description (user story) of this PBI
    user_story=models.CharField(max_length=400,default="")

    #Confirmation of this PBI
    confirmation=models.CharField(max_length=400,default="")

class Project_info(models.Model):
    #Current sprint number e.g. First sprint is sprint #1
    sprint_no=models.IntegerField(default=1)

    #Ending time of the current sprint
    sprint_end_time=models.DateTimeField(max_length=400,default="")

    #Duration of a single sprint
    sprint_Duration=models.IntegerField(default=1)


