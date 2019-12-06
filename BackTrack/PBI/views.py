from django.shortcuts import render, redirect
from .forms import PB_itemForm, create_sprint_form
from .models import PB_item, Project_info, Sprint
from login.models import currentUser
from django.utils.html import strip_tags
# Create your views here.

# The main view that displays all PBIs (the backlog view)
def backlog_view(request,*args,**kwargs):
    # Get current user info
    user = currentUser.objects.all()[0]
    if user.userType == 1:
        productOwner = True
    else:
        productOwner = False

    # Get Total Story Points
    PBI_all = PB_item.objects.all()
    totalStoryPoints = 0
    for PBI in PBI_all:
        totalStoryPoints += PBI.story_point

    # Get Finished Story Points
    PBI_finished = PB_item.objects.filter(status="Finished")
    finishedStoryPoints = 0
    for PBI in PBI_finished:
        finishedStoryPoints += PBI.story_point

    # Check if user is allowed to create sprint
    # only if no sprint is active
    if Sprint.objects.filter(status="active").exists():
        activeSprintExists = True
    else:
        activeSprintExists = False

    # Get Lowest Priority
    lowestPriority = PB_item.objects.all().latest("priority_no").priority_no

    context={
        "PBI_all":PBI_all,
        "total_story_points":totalStoryPoints,
        "finished_story_points":finishedStoryPoints,
        "activeSprintExists": activeSprintExists,
        "lowestPriority": lowestPriority,
        "username": user.username,
        "productOwner": productOwner,
    }

    return render(request,"PBI_backlog.html",context)


# The view to add a PBI
def add_view(request,*args,**kwargs):
    # Get current user info
    user = currentUser.objects.all()[0]
    if user.userType == 1:
        productOwner = True
    else:
        productOwner = False

    # Get Lowest Priority
    lowestPriority = PB_item.objects.all().latest("priority_no").priority_no
    form=PB_itemForm(request.POST or None, initial={
        "priority_no": lowestPriority + 1
    })
    if form.is_valid():
        form.priority_no=lowestPriority+1
        form.save()
        return redirect('../')
    context={
        'form':form,
        "username": user.username,
        "productOwner": productOwner,
        }
    return render(request,"PBI_form.html",context)


# The view to display details for a certain PBI (for editing)
def edit_view(request, id):
    # Get current user info
    user = currentUser.objects.all()[0]
    if user.userType == 1:
        productOwner = True
    else:
        productOwner = False

    PBI=PB_item.objects.get(id=id)
    form=PB_itemForm(request.POST or None,initial={
        'name':PBI.name,
        'status':PBI.status,
        'story_point':PBI.story_point,
        'user_story':PBI.user_story,
        'confirmation':PBI.confirmation
        })

    if form.is_valid():
        PBI.name=form.cleaned_data['name']
        PBI.status=form.cleaned_data['status']
        PBI.story_point=form.cleaned_data['story_point']
        PBI.user_story=form.cleaned_data['user_story']
        PBI.confirmation=form.cleaned_data['confirmation']
        PBI.save()
        return redirect('../')
    context={
        'form':form,'placeholder':PBI,
        "username": user.username,
        "productOwner": productOwner,
        }

    return render(request,"PBI_form.html",context)

# The view to delete a PBI
def delete_view(request,id):
    PB_item.objects.filter(id=id).delete()
    context={"item":PB_item.objects.all()}
    return redirect('../')

# To create a new sprint
def create_sprint(request):
    # Get current user info
    user = currentUser.objects.all()[0]
    if user.userType == 1:
        productOwner = True
    else:
        productOwner = False

    # Get the current sprint number
    sprints = Sprint.objects.all()
    if sprints.exists():
        current_sprint_no = sprints.latest("id").sprint_no
    else:
        current_sprint_no = 0
    # Create the form for user to input capacity of the sprint, increment sprint_no by 1
    form=create_sprint_form(request.POST or None, initial={
        "sprint_no": current_sprint_no + 1,
        "status": "active"
    })

    # Save
    if form.is_valid():
        form.save()
        return redirect('../')
    context={
        'form': form,
        "username": user.username,
        "productOwner": productOwner,
        }
    return render(request, "PBI_form.html", context)

def add_PBI_to_current_sprint(request, id):
    # Get the current sprint number
    sprints = Sprint.objects.all()
    if sprints.exists():
        current_sprint_no = sprints.latest("id").sprint_no
    else:
        current_sprint_no = 0

    PBI = PB_item.objects.get(id=id)
    PBI.sprint_no = current_sprint_no
    PBI.status = "In Progress"
    PBI.save()
    return redirect("../")

def movePBIup(request, id):
    # PBI selected. (It is lower in the PBI table)
    lowerPBI = PB_item.objects.get(id=id)
    lowerPriority = lowerPBI.priority_no
    # PBI to be swapped. (It is on top of the selected lower PBI)
    upperPriority = lowerPBI.priority_no - 1
    upperPBI = PB_item.objects.get(priority_no=upperPriority)
    # Swap their priorities
    upperPBI.priority_no = 0 # To avoid violating unique constraint on priority_no
    upperPBI.save()
    lowerPBI.priority_no = upperPriority
    lowerPBI.save()
    upperPBI.priority_no = lowerPriority
    upperPBI.save()
    return redirect('../')

def movePBIdown(request, id):
    # PBI selected. (It is upper in the PBI table)
    upperPBI = PB_item.objects.get(id=id)
    upperPriority = upperPBI.priority_no
    # PBI to be swapped. (It is below the selected lower PBI)
    lowerPriority = upperPBI.priority_no + 1
    lowerPBI = PB_item.objects.get(priority_no=lowerPriority)
    # Swap their priorities
    upperPBI.priority_no = 0 # To avoid violating unique constraint on priority_no
    upperPBI.save()
    lowerPBI.priority_no = upperPriority
    lowerPBI.save()
    upperPBI.priority_no = lowerPriority
    upperPBI.save()
    return redirect('../')
