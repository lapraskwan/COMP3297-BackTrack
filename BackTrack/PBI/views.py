from django.shortcuts import render ,redirect
from .forms import PB_itemForm, PB_editForm
from .models import PB_item
from django.utils.html import strip_tags
# Create your views here.
def main_view(request,*args,**kwargs):
    context={"item":PB_item.objects.all()}


    return render(request,"show_all.html",context)

def detail_view(request, id):
    form=PB_item.objects.get(id=id)
    update=PB_editForm(request.POST or None,initial={'feature':form.feature,'status':form.status,'priority':form.priority,'story_point':form.story_point})
    #print(update)
    if update.is_valid():
        data=update.cleaned_data
        print(data)
        form.feature=update.cleaned_data['feature']
        form.status=update.cleaned_data['status']
        form.priority=update.cleaned_data['priority']
        form.story_point=update.cleaned_data['story_point']
        form.save()
        return redirect('../')
    context={'form':update,'placeholder':form}

    return render(request,"detail.html",context)

def delete_view(request,id):
    form=PB_item.objects.filter(id=id).delete()
    context={"item":PB_item.objects.all()}
    return redirect('../')



def add_view(request,*args,**kwargs):
    form=PB_itemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../PBI/')
    context={'form':form}
    return render(request,"pbiadd.html",context)
