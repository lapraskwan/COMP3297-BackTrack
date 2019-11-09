from django.shortcuts import render ,redirect
from .forms import PB_itemForm, PB_editForm
from .models import PB_item
from django.utils.html import strip_tags
# Create your views here.

# The main view that displays all PBIs (the backlog view)
def backlog_view(request,*args,**kwargs):
    PBI_all = PB_item.objects.all()
    totalStoryPoints = 0
    for item in PBI_all:
        totalStoryPoints += item.story_point
    
    PBI_upcoming = PB_item.objects.exclude(status="Finished")
    remainingStoryPoints = 0
    for item in PBI_upcoming:
        remainingStoryPoints += item.story_point

    context={
        "PBI_all":PBI_all,
        "PBI_upcoming":PBI_upcoming,
        "Total_story_points":totalStoryPoints,
        "Cumulative_story_points":totalStoryPoints-remainingStoryPoints,
    }

    return render(request,"PBI_backlog.html",context)


# The view to add a PBI
def add_view(request,*args,**kwargs):
    form=PB_itemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context={'form':form}
    return render(request,"PBI_add.html",context)


# The view to display details for a certain PBI (for editing)
def edit_view(request, id):
    form=PB_item.objects.get(id=id)
    update=PB_editForm(request.POST or None,initial={'name':form.name,'status':form.status,'priority_no':form.priority_no,'story_point':form.story_point,'story_point':form.user_story,'story_point':form.confirmation})
    #print(update)
    if update.is_valid():
        data=update.cleaned_data
        form.name=update.cleaned_data['name']
        form.status=update.cleaned_data['status']
        form.priority_no=update.cleaned_data['priority_no']
        form.story_point=update.cleaned_data['story_point']
        form.user_story=update.cleaned_data['user_story']
        form.confirmation=update.cleaned_data['confirmation']
        form.save()
        return redirect('../')
    context={'form':update,'placeholder':form}

    return render(request,"PBI_add.html",context)

# The view to delete a PBI
def delete_view(request,id):
    form=PB_item.objects.filter(id=id).delete()
    context={"item":PB_item.objects.all()}
    return redirect('../')
