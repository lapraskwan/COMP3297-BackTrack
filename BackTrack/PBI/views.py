from django.shortcuts import render ,redirect
from .forms import PB_itemForm, PB_editForm
from .models import PB_item
from django.utils.html import strip_tags
# Create your views here.

# The main view that displays all PBIs (the backlog view)
def backlog_view(request,*args,**kwargs):
    context={
        "PBI_all":PB_item.objects.all(),
        "PBI_upcoming":PB_item.objects.exclude(status="Finished")}
    return render(request,"backlog.html",context)


# The view to add a PBI
def add_view(request,*args,**kwargs):
    form=PB_itemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context={'form':form}
    return render(request,"add.html",context)


# The view to display details for a certain PBI (for editing)
def detail_view(request, id):
    form=PB_item.objects.get(id=id)
    update=PB_editForm(request.POST or None,initial={'name':form.feature,'status':form.status,'priority_no':form.priority_no,'story_point':form.story_point})
    #print(update)
    if update.is_valid():
        data=update.cleaned_data
        form.feature=update.cleaned_data['feature']
        form.status=update.cleaned_data['status']
        form.priority=update.cleaned_data['priority']
        form.story_point=update.cleaned_data['story_point']
        form.save()
        return redirect('../')
    context={'form':update,'placeholder':form}

    return render(request,"detail.html",context)

# The view to delete a PBI
def delete_view(request,id):
    form=PB_item.objects.filter(id=id).delete()
    context={"item":PB_item.objects.all()}
    return redirect('../')
