from django.db import models

# Create your models here.
class PB_item(models.Model):
    # Name of this PBI
    name=models.CharField(max_length=100)

    # Set the choices of status of PBI. (actual value, readable name)
    PBIstatusChoices = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Finished", "Finished"),
        ("Unfinished", "Unfinished")
    ]
    # Status of this PBI, e.g. "Finished"
    status=models.CharField(max_length=100, choices=PBIstatusChoices, default="Pending", blank=True)

    # Priority number of this PBI, i.e. the most important feature has priority 1, the second most has priority 2, etc
    priority_no=models.IntegerField(unique=True)

    # Story point estimation of this PBI
    story_point=models.IntegerField(default=1)

    # Description (user story) of this PBI
    user_story=models.CharField(max_length=400,default="")

    # Confirmation of this PBI
    confirmation=models.CharField(max_length=400,default="")

    # Sprint Number
    sprint_no=models.IntegerField(null=True, blank=True)

    class Meta:
        ordering=['priority_no']

class Project_info(models.Model):
    # Current sprint number e.g. First sprint is sprint #1
    sprint_no=models.IntegerField(default=1)

    # Ending time of the current sprint
    sprint_end_time=models.DateTimeField(max_length=400,default="")

    # Duration of a single sprint
    sprint_Duration=models.IntegerField(default=1)

class Sprint(models.Model):
    # Sprint Number
    sprint_no=models.IntegerField()

    # Capacity
    capacity=models.IntegerField()

    # Set the choices of status of sprint. (actual value, readable name)
    sprintStatusChoices = [
        ("active", "Active"),
        ("ended", "Ended")
    ]
    # Status
    status=models.CharField(max_length=100, choices=sprintStatusChoices, default="active")

    # ### FOR FUTURE USE ###
    # # Start Time
    # start_time=models.DateTimeField(max_length=400,default="")

    # # End Time
    # end_time=models.DateTimeField(max_length=400,default="")
