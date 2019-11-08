from django import forms

from .models import PB_item


class PB_itemForm(forms.ModelForm):
    class Meta:
        model=PB_item
        fields=[
            'name','status','priority_no','story_point','user_story','confirmation'
        ]

class PB_editForm(forms.ModelForm):
    class Meta:
        model=PB_item
        fields=[
            'name','status','priority_no','story_point','user_story','confirmation'
        ]
