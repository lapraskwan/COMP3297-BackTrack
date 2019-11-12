from django import forms

from .models import PB_item, Sprint


class PB_itemForm(forms.ModelForm):
    class Meta:
        model=PB_item
        fields=[
            'name','status','priority_no','story_point', 'user_story','confirmation', 'sprint_no'
        ]
        widgets = {
            'status': forms.HiddenInput(),
            'priority_no': forms.HiddenInput(),
            'sprint_no': forms.HiddenInput()
            }

class create_sprint_form(forms.ModelForm):
    class Meta:
        model=Sprint
        fields=[
            'sprint_no', 'capacity', 'status'
        ]
        widgets = {
            'sprint_no': forms.HiddenInput(),
            'status': forms.HiddenInput()
            }
