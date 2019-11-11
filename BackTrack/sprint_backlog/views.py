from django.shortcuts import render, redirect
from django.contrib import messages
from .models import sprint_backlog_item
from PBI.models import PB_item, Sprint
from .forms import sprint_backlog_item_form

# Create your views here.



def backlog_view(request):
    # Get info of the current sprint
    sprints = Sprint.objects.all()
    if sprints.exists():
        currentSprintNumber = sprints.latest("id").sprint_no
        capacity = sprints.latest("id").capacity
    else:
        currentSprintNumber = 0
        capacity = 0

    # Get all PBIs that are in progress in the sprint
    inProgressPBIItems = PB_item.objects.filter(sprint_no=currentSprintNumber)
    # Get the PBI ids
    inProgressPBIIds = []
    for PBI in inProgressPBIItems:
        inProgressPBIIds.append(PBI.id)
        # Check if all items are finished
        sprintBacklogItems = sprint_backlog_item.objects.filter(PBI=PBI.id)
        if all(item.status == "Finished" for item in sprintBacklogItems) and sprintBacklogItems:
            PBI.status = "Finished"
            PBI.save()
        else:
            PBI.status = "In Progress"
            PBI.save()
        
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=inProgressPBIIds)
    # Calculate the total estimation, and finished estimation (finished work)
    totalEstimation = 0
    finishedEstimation = 0
    for item in sprintBacklogItems:
        totalEstimation += item.estimation
        if item.status == "Finished":
            finishedEstimation += item.estimation
    # Remaining Estimation
    remainingEstimation = totalEstimation - finishedEstimation
    if totalEstimation != 0:
        # Finished Percentage
        finishedPercentage = round(finishedEstimation / totalEstimation * 100, 1)
        # Remaining Percentage
        remainingPercentage = round(remainingEstimation / totalEstimation * 100, 1)
    else:
        finishedPercentage = 0
        remainingPercentage = 100
    # Remaining Capacity
    remainingCapacity = capacity - totalEstimation

    # Alert if the sum of estimation is larger than the capacity of this sprint
    if totalEstimation > capacity:
        alert_flag_2 = True
        disableButton = True
    elif totalEstimation == capacity:
        alert_flag_2 = False
        disableButton = True
    else:
        alert_flag_2 = False
        disableButton = False
    # Return
    context={
        "currentSprintNumber": currentSprintNumber,
        "capacity": capacity, 
        "remainingCapacity": remainingCapacity,
        "totalEstimation": totalEstimation, 
        "finishedEstimation": finishedEstimation,
        "remainingEstimation": remainingEstimation,
        "finishedPercentage": finishedPercentage,
        "remainingPercentage": remainingPercentage,
        "PBI": inProgressPBIItems, 
        "item": sprintBacklogItems, 
        "alert_flag_2": alert_flag_2, 
        "disableButton": disableButton
        }
    return render(request, "Sprint_backlog.html", context)

def add_view(request, id):
    # Get info of the current sprint
    sprints = Sprint.objects.all()
    if sprints.exists():
        currentSprintNumber = sprints.latest("id").sprint_no
        capacity = sprints.latest("id").capacity
    else:
        currentSprintNumber = 0
        capacity = 0
    
    # Create form
    form=sprint_backlog_item_form(request.POST or None, initial={"PBI": id})

    # Get all PBIs that are in progress in the sprint
    inProgressPBIItems = PB_item.objects.filter(sprint_no=currentSprintNumber)
    # Get the PBI ids
    inProgressPBIIds = []
    for PBI in inProgressPBIItems:
        inProgressPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=inProgressPBIIds)
    # Calculate the sum of estimation
    totalEstimation = 0
    for item in sprintBacklogItems:
        totalEstimation += item.estimation
    # Alert if the sum of estimation is larger than the capacity of this sprint
    if totalEstimation >= capacity:
        # Return
        return redirect('../')
    
    # Get all PBIs that are in progress in the sprint
    inProgressPBIItems = PB_item.objects.filter(sprint_no=currentSprintNumber)
    # Get the PBI ids
    inProgressPBIIds = []
    for PBI in inProgressPBIItems:
        inProgressPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=inProgressPBIIds)
    # Calculate the total estimation, and finished estimation (finished work)
    totalEstimation = 0
    finishedEstimation = 0
    for item in sprintBacklogItems:
        totalEstimation += item.estimation
    # Remaining Capacity
    remainingCapacity = capacity - totalEstimation

    # Determine what to do with the form
    if form.is_valid():
        if form.cleaned_data["estimation"] + totalEstimation > capacity:
            # Return
            context={
                'form': form, 
                "capacity": capacity, 
                "remainingCapacity": remainingCapacity, 
                "alert_flag_1": True
                }
            return render(request, "Sprint_form.html", context)
        else:
            form.save()
            return redirect('../')
    context={
        'form':form,
        "capacity": capacity, 
        "remainingCapacity": remainingCapacity,
        }
    return render(request,"Sprint_form.html",context)

def delete_view(request, id):
    # Delete the sprint backlog item with the given id
    sprint_backlog_item.objects.filter(id=id).delete()
    # Return
    return redirect("../")

def edit_view(request, id):
    # Get info of the current sprint
    sprints = Sprint.objects.all()
    if sprints.exists():
        currentSprintNumber = sprints.latest("id").sprint_no
        capacity = sprints.latest("id").capacity
    else:
        currentSprintNumber = 0
        capacity = 0
    
    # Get the sprint backlog item with the given id
    item=sprint_backlog_item.objects.get(id=id)
    # Create a form with proper initials
    form=sprint_backlog_item_form(request.POST or None,initial={
        'PBI': item.PBI, 
        'title':item.title,
        'status':item.status,
        'owner':item.owner,
        'estimation':item.estimation
        })
    
    # Get all PBIs that are in progress in the sprint
    inProgressPBIItems = PB_item.objects.filter(sprint_no=currentSprintNumber)
    # Get the PBI ids
    inProgressPBIIds = []
    for PBI in inProgressPBIItems:
        inProgressPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=inProgressPBIIds)
    # Calculate the sum of estimation
    totalEstimation = 0
    for sprintItem in sprintBacklogItems:
        totalEstimation += sprintItem.estimation
        if sprintItem == item:
            originalItemEstimation = sprintItem.estimation
    # Remaining Capacity
    remainingCapacity = capacity - totalEstimation
    
    # Determine what to do with the form
    if form.is_valid():
        if form.cleaned_data["estimation"] + totalEstimation - originalItemEstimation > capacity:
            # Return
            context={'form': form, "alert_flag_1": True}
            return render(request, "Sprint_form.html", context)
        else:
            item.title=form.cleaned_data['title']
            item.status=form.cleaned_data['status']
            item.owner=form.cleaned_data['owner']
            item.estimation=form.cleaned_data['estimation']
            item.save()
            return redirect('../')
        
    context={
        'form':form,
        "capacity": capacity, 
        "remainingCapacity": remainingCapacity,
        }

    return render(request,"Sprint_form.html",context)

def pushPBIBack_view(request, id):
    PBI = PB_item.objects.get(id=id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI=PBI.id)
    # Change the status of PBI.
    if all(item.status == "Pending" for item in sprintBacklogItems): # Haven't done anything on the PBI yet
        PBI.status = "Pending"
    else: # Done something on the PBI
        # Set status of in progress items to unfinished
        for item in sprintBacklogItems:
            if item.status == "In Progress":
                item.status = "Unfinished"
                item.save()
        PBI.status = "Unfinished"
    # Save
    PBI.sprint_no = None
    PBI.save()
    # Return
    return redirect('../')

def endSprint(request):
    # Get info of the current sprint
    sprints = Sprint.objects.all()
    if sprints.exists():
        currentSprintNumber = sprints.latest("id").sprint_no
        capacity = sprints.latest("id").capacity
    else:
        currentSprintNumber = 0
        capacity = 0

    # Get all PBIs that are in progress in the sprint
    inProgressPBIItems = PB_item.objects.filter(sprint_no=currentSprintNumber)
    
    for PBI in inProgressPBIItems:
        # Get the sprint backlog items that belongs to this sprint
        sprintBacklogItems = sprint_backlog_item.objects.filter(PBI=PBI.id)
        # Change the status of PBI.
        if all(item.status == "Pending" for item in sprintBacklogItems): # Haven't done anything on the PBI yet
            PBI.status = "Pending"
            PBI.save()
        elif all(item.status == "Finished" for item in sprintBacklogItems) and sprintBacklogItems:
            PBI.status = "Finished"
            PBI.save()
        else: # Done something on the PBI
            # Set status of in progress items to unfinished
            for item in sprintBacklogItems:
                if item.status == "In Progress":
                    item.status = "Unfinished"
                    item.save()
            PBI.status = "Unfinished"
            PBI.save()
        
    # Change Sprint status
    currentSprint = Sprint.objects.all().latest("id")
    currentSprint.status = "ended"
    currentSprint.save()

    return redirect('../../PBI')

def doneSprintItem(request, id):
    item = sprint_backlog_item.objects.get(id=id)
    item.status = "Finished"
    item.save()
    return redirect('../')