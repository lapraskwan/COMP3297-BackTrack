from django.shortcuts import render, redirect
from django.contrib import messages
from .models import sprint_backlog_item, capacity
from PBI.models import PB_item
from .forms import sprint_backlog_item_form

# Create your views here.
capacity = capacity.objects.filter(id=1)[0].capacity

def showAll(request):
    # Get all PBIs that are in progress in the sprint
    pendingPBIItems = PB_item.objects.filter(status="pending")
    # Get the PBI ids
    pendingPBIIds = []
    for PBI in pendingPBIItems:
        pendingPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=pendingPBIIds)
    # Calculate the total estimation, and finished estimation (finished work)
    totalEstimation = 0
    finishedEstimation = 0
    for item in sprintBacklogItems:
        totalEstimation += item.estimation
        if item.status == "Finished":
            finishedEstimation += item.estimation
    # Remaining Estimation
    remainingEstimation = totalEstimation - finishedEstimation
    # Finished Percentage
    finishedPercentage = finishedEstimation / totalEstimation * 100
    # Remaining Percentage
    remainingPercentage = remainingEstimation / totalEstimation * 100
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
        "capacity": capacity, 
        "remainingCapacity": remainingCapacity,
        "totalEstimation": totalEstimation, 
        "finishedEstimation": finishedEstimation,
        "remainingEstimation": remainingEstimation,
        "finishedPercentage": finishedPercentage,
        "remainingPercentage": remainingPercentage,
        "PBI": pendingPBIItems, 
        "item": sprintBacklogItems, 
        "alert_flag_2": alert_flag_2, 
        "disableButton": disableButton
        }
    return render(request, "showAll.html", context)

def add(request, id):
    form=sprint_backlog_item_form(request.POST or None, initial={"PBI": id})

    # Get all PBIs that are in progress in the sprint
    pendingPBIItems = PB_item.objects.filter(status="pending")
    # Get the PBI ids
    pendingPBIIds = []
    for PBI in pendingPBIItems:
        pendingPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=pendingPBIIds)
    # Calculate the sum of estimation
    totalEstimation = 0
    for item in sprintBacklogItems:
        totalEstimation += item.estimation
    # Alert if the sum of estimation is larger than the capacity of this sprint
    if totalEstimation >= capacity:
        # Return
        return redirect('../')

    # Determine what to do with the form
    if form.is_valid():
        if form.cleaned_data["estimation"] + totalEstimation > capacity:
            # Return
            context={'form': form, "alert_flag_1": True}
            return render(request, "addSprintItem.html", context)
        else:
            form.save()
            return redirect('../')
    context={'form':form}
    return render(request,"addSprintItem.html",context)

def delete(request, id):
    # Delete the sprint backlog item with the given id
    sprint_backlog_item.objects.filter(id=id).delete()
    # Return
    return redirect("../")

def update(request, id):
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
    pendingPBIItems = PB_item.objects.filter(status="pending")
    # Get the PBI ids
    pendingPBIIds = []
    for PBI in pendingPBIItems:
        pendingPBIIds.append(PBI.id)
    # Get the sprint backlog items that belongs to this sprint
    sprintBacklogItems = sprint_backlog_item.objects.filter(PBI__in=pendingPBIIds)
    # Calculate the sum of estimation
    totalEstimation = 0
    for sprintItem in sprintBacklogItems:
        if sprintItem != item:
            totalEstimation += sprintItem.estimation
    
    # Determine what to do with the form
    if form.is_valid():
        if form.cleaned_data["estimation"] + totalEstimation > capacity:
            # Return
            context={'form': form, "alert_flag_1": True}
            return render(request, "addSprintItem.html", context)
        else:
            item.title=form.cleaned_data['title']
            item.status=form.cleaned_data['status']
            item.owner=form.cleaned_data['owner']
            item.estimation=form.cleaned_data['estimation']
            item.save()
            return redirect('../')
        
    context={'form':form}

    return render(request,"addSprintItem.html",context)

def pushPBIBack(request, id):
    PBI = PB_item.objects.get(id=id)
    PBI.status = "pending"
    PBI.save()
    # Return
    return redirect('../')
